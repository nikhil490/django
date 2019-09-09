from django.shortcuts import render
from articles.models import Article


def homepage(request):
    articles = Article.objects.all().order_by('types')
    return render(request, 'index.html', {'articles': articles})


def about(request):
    return render(request, 'about.html')


def contact(request):

    return render(request, 'contact.html')


