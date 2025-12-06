from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

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