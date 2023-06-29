from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from Fresh_Airlines.accounts.forms import RegistrationForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash

from Fresh_Airlines.wallet.models import Wallet


def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                if not Wallet.objects.get(user=user):
                    wallet = Wallet(user=user)
                    wallet.save()
                return render(request, template_name='common/home-page-when-login.html')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login-page.html', {'form': form})


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'common/registration-successfull.html')
    else:
        form = RegistrationForm()

    return render(request, 'accounts/register-page.html', {'form': form})


def profile_view(request):
    user = request.user
    return render(request, 'accounts/profile.html', {'user': user})


def logout_view(request):
    logout(request)
    return render(request, template_name='common/home-page.html')


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return redirect('profile')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'accounts/change_password.html', {'form': form})

