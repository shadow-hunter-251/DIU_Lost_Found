from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import redirect, render

from .forms import RegisterForm


def register_view(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            user = form.save()

            messages.success(
                request,
                'Your account has been created successfully.'
            )

            login(request, user)

            return redirect('home')

    else:
        form = RegisterForm()

    return render(
        request,
        'accounts/register.html',
        {'form': form}
    )


def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)

            return redirect('home')

        messages.error(
            request,
            'Invalid username or password.'
        )

    return render(request, 'accounts/login.html')


def logout_view(request):
    logout(request)

    messages.success(
        request,
        'You have been logged out.'
    )

    return redirect('home')


@login_required
def profile_view(request):
    return render(
        request,
        'accounts/profile.html'
    )