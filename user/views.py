from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegisterForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save(commit=False)
            email=form.cleaned_data['email']
            form.save()
            return redirect('login')

    else:
        form = RegisterForm()
    return render(request,"users/register.html", {'form': form})

@login_required
def profileView(request):
    owner = request.user
    return render(request,template_name='users/profile.html', context={'owner': owner})











