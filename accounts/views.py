from .forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth import login as user_login
from django.contrib.auth import logout as user_logout
from django.contrib.auth.decorators import login_required
# from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.conf import settings

# Create your views here.
def signup(request):
    if request.method == "POST":
        user_form = UserCreationForm(request.POST)
        if user_form.is_valid():
            user = user_form.save()
            return redirect('posts:list')
    else:    
        user_form = UserCreationForm()
    context = {'user_form': user_form}
    return render(request, 'accounts/forms.html', context)
    
def detail(request, user_pk):
    user = User.objects.get(pk=user_pk)
    context = {'user': user}
    return render(request, 'accounts/detail.html', context)
    
def login(request):
    if request.method == "POST":
        signin_form = AuthenticationForm(request, request.POST)
        if signin_form.is_valid():
            user_login(request, signin_form.get_user())
            return redirect('posts:list')
    signin_form = AuthenticationForm()
    context = {'user_form': signin_form}
    return render(request, 'accounts/forms.html', context)
    
@login_required
def logout(request):
    user_logout(request)
    return redirect('posts:list')