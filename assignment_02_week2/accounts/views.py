from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import auth

# Create your views here.
def register(request):
    if request.method == 'POST':
        userform = UserCreationForm(request.POST)
        if userform.is_valid():
            userform.save()
            return redirect('home')
    userform = UserCreationForm()
    context = {
        'userform': userform
    }
    return render(request, 'accounts/register.html', context)


def login(request):
    if request.method == 'POST':
        userform = AuthenticationForm(request, request.POST)   
        if userform.is_valid():
            user = userform.get_user()
            auth.login(request, user)
            return redirect('home')
    else:
        userform = AuthenticationForm()
    userform = AuthenticationForm()
    context = {
        'userform': userform
    }
    return render(request, 'accounts/login.html', context)