from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from .forms import PostForm, ImageForm
from django.forms import widgets, ModelForm

# Create your views here.
def list(request):
    posts = Post.objects.order_by('-pk')
    context = {'posts': posts}
    return render(request, 'posts/list.html', context)
    
def create(request):
    if request.method == "POST":
        post_form = PostForm(request.POST, request.FILES)
        image_form = ImageForm(request.POST, request.FILES)
        if post_form.is_valid() and image_form.is_valid():
            post = post_form.save()
            image = image_form.save()
            return redirect('posts:list')
    else:
        post_form = PostForm()
        image_form = ImageForm()
    context = {'post_form': post_form, 'image_form': image_form}
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