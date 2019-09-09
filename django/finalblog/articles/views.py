from django.shortcuts import render, get_object_or_404, redirect
from .models import Article
from .forms import PostForm, CommentForm, AnonymousCommentForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (DeleteView)
from django.contrib import messages


def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    return render(request, 'post_detail.html', {'articles': article})


def article_each(request, types):
    limit = str(types)
    article = Article.objects.all().filter(types=limit)
    return render(request, 'articles/listofeach.html', {'article': article})


@login_required(login_url="/accounts/login/")
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PostForm()
    return render(request, 'articles/article_create.html', {'form': form})


def add_comment_to_post(request, pk):
    post = get_object_or_404(Article, pk=pk)
    if request.user.is_authenticated:
        username = request.user.username
        if request.method == "POST":
            form = CommentForm(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.post = post
                comment.author = username
                comment.save()
                return redirect('articles:detail', pk)
        else:
            form = CommentForm()
        return render(request, 'articles/add_comment_to_post.html', {'form': form})
    else:
           if request.method == "POST":
                form = AnonymousCommentForm(request.POST)
                if form.is_valid():
                    comment = form.save(commit=False)
                    comment.post = post
                    comment.author = "Anonymous-"+str(pk)
                    comment.save()
                    return redirect('articles:detail', pk)
           else:
                form = AnonymousCommentForm(request.POST)
           return render(request, 'articles/add_comment_to_post.html', {'form': form})


def PostUpdateView(request, pk):
    obj = get_object_or_404(Article, pk=pk)
    form = PostForm(request.POST or None, instance=obj)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.save()
        messages.success(request, "You successfully updated the post")

        return render(request, 'post_detail.html', {'articles': obj})
    else:
        error = 'The form was not updated successfully. Please enter in a title and content'
        context = {'form': form, 'error': error}
        return render(request, 'articles/update.html', context)


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Article
    success_url = '/'

    def test_func(self):
        article = self.get_object()
        if self.request.user == article.Author:
            return True
        return False


