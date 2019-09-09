from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth import logout


def signup_view(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            email = form.cleaned_data.get('email')
            userProfile = user.profile
            userProfile.save()

            messages.success(request, f'Your account has been created. You are now enable to Log In')
            return redirect('home')
    else:
        form = UserRegisterForm()
    return render(request, 'accounts/signup.html', {'form': form})


def profile(request):

    myprofile = request.user.profile
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            image = p_form.cleaned_data.get('image')
            myprofile.image = image
            myprofile.save()
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('accounts:profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form,

    }
    return render(request, 'accounts/profile.html', context)


def logout_view(request):
            logout(request)
            return redirect('home')
