from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from .forms import PostForm
from django.forms import widgets, ModelForm

# Create your views here.
def list(request):
    posts = Post.objects.order_by('-pk')
    context = {'posts': posts}
    return render(request, 'posts/list.html', context)
    
def create(request):
    if request.method == "POST":
        post_form = PostForm(request.POST, request.FILES)
        print(post_form)
        print(post_form.is_valid)
        if post_form.is_valid():
            post = post_form.save()
            return redirect('posts:list')
    else:
        post_form = PostForm()
    context = {'post_form': post_form}
    return render(request, 'posts/form.html', context)

def detail(request, posts_pk):
    post = get_object_or_404(Post, pk=posts_pk)
    context = {'post': post}
    return render(request, 'posts/detail.html', context)
    
def edit(request, posts_pk):
    post = get_object_or_404(Post, pk=posts_pk)
    if request.method == "POST":
        post_form = PostForm(request.POST, instance=post)
        post_form.save()
        return redirect('posts:list')
    else:
        post_form = PostForm(instance=post)
    context = {'post_form': post_form}
    return render(request, 'posts/form.html', context)

def delete(request, posts_pk):
    post = get_object_or_404(Post, pk=posts_pk)
    post.delete()
    return redirect('posts:list')