from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth import login as user_login
from django.contrib.auth import logout as user_logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
# from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.conf import settings

from .forms import UserCustomCreationForm, AuthenticationForm, ProfileForm
from .models import Profile

# Create your views here.
@require_http_methods(['GET', 'POST'])
def signup(request):
    if request.user.is_authenticated:
        return redirect('posts:list')
    if request.method == "POST":
        user_form = UserCustomCreationForm(request.POST)
        if user_form.is_valid():
            user = user_form.save()
            Profile.objects.create(user=user)
            user_login(request, user)
            return redirect('accounts:profile_update')
    else:    
        user_form = UserCustomCreationForm()
    context = {'user_form': user_form}
    return render(request, 'accounts/forms.html', context)
    
    
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

@login_required
def list(request):
    # users = User.objects.all()
    User = get_user_model()
    users = User.objects.all()
    context = {'users': users}
    return render(request, 'accounts/list.html', context)

@login_required
def profile_update(request):
    if request.method == 'POST':
        # data=request.FIELS 로 해도 됌 키워드로
        profile_form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if profile_form.is_valid():
            profile_form.save()
            return redirect('accounts:profile')
    profile_form = ProfileForm(instance=request.user.profile)
    context = {'profile_form': profile_form}
    return render(request, 'accounts/profile_update.html', context)
    
@login_required
def profile(request):
    return render(request, 'accounts/profile.html')
    
def detail(request, user_pk):
    User = get_user_model()
    user = get_object_or_404(User, pk=user_pk)
    context = {'user_info': user}
    return render(request, 'accounts/detail.html', context)
    
@login_required
def follow(request, user_pk):
    User = get_user_model()
    target_user = get_object_or_404(User, pk=user_pk)
    if request.user in target_user.followers.all():
        target_user.followers.remove(request.user)
    else:
        target_user.followers.add(request.user)
    # print(request.resolver_match.url_name)
    return redirect('accounts:detail', user_pk)

@login_required
def search(request):
    # 1. 내가 만들어놓은 모델 -> DB
    # 2. variable routing (X)
    # 3. form (O)
    username = request.GET.get('username')
    User = get_user_model()
    user = User.objects.filter(username=username).first()
    if not user:
        print('3241')
        messages.warning(request, f'{username}을 찾을 수 없습니다.')
        return redirect('posts:list')
    return redirect('accounts:detail', user.pk)