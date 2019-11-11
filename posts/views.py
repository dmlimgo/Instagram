from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Image, Comment
from .forms import PostForm, ImageForm
from django.forms import widgets, ModelForm
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.db.models import Q

# Create your views here.
@login_required
def list(request):
    # from django.db.models import Q
    posts = Post.objects.filter(
                        Q(user__in=request.user.followings.values('id'))
                        | Q(user=request.user.id)
                        ).order_by('-pk')
    User = get_user_model()
    users = User.objects.all()
    context = {'posts': posts, 'users': users}
    return render(request, 'posts/list.html', context)
# @login_required
# def list(request):
#     if request.user.is_authenticated:
#         posts = Post.objects.order_by('-pk')
#         context = {'posts': posts}
#         return render(request, 'posts/list.html', context)
#     else:
#         return redirect('accounts:login')

@login_required
def create(request):
    if request.method == "POST":
        post_form = PostForm(request.POST)
        # 할 필요 없음
        # image_form = ImageForm(request.POST, request.FILES)
        if post_form.is_valid():
            
            post = post_form.save(commit=False)
            post.user = request.user
            post.save()
            # 만약 여러개의 파일을 받고 싶다면 FILES안의 getlist로 받을 수 있다.
            files = request.FILES.getlist('file')
            for file in files:
                request.FILES['file'] = file
                # 위치 인자로 넘겨주려고 했던건데
                # image_form = ImageForm(request.POST, request.FILES)
                # 파일인자로 넘겨줘도 된다.
                image_form = ImageForm(files=request.FILES)
                if image_form.is_valid():
                    image = image_form.save(commit=False)
                    image.post = post
                    image.thumbnail_fill = request.FILES.get('file')
                    print(image.thumbnail_fill)
                    print(image.thumbnail_fill.url)
                    image.save()
                    print(image.thumbnail_fill)
                    print(image.thumbnail_fill.url)
            # return redirect('posts:detail', post.pk)
            # 더 나은방법
            # return redirect(post)
            return redirect('posts:list')
    else:
        post_form = PostForm()
        image_form = ImageForm()
    context = {'post_form': post_form, 'image_form': image_form}
    return render(request, 'posts/form.html', context)

@login_required
def detail(request, posts_pk):
    post = get_object_or_404(Post, pk=posts_pk)
    context = {'post': post}
    return render(request, 'posts/detail.html', context)

@login_required    
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

@login_required
def delete(request, posts_pk):
    post = get_object_or_404(Post, pk=posts_pk)
    post.delete()
    return redirect('posts:list')

@login_required
def like(request, posts_pk):
    post = get_object_or_404(Post, pk=posts_pk)
    user = request.user
    # user가 지금 해당 게시글에 좋아요를 한 적이 있는지?
    # if user in post.like_users.all():
    #     post.like_users.remove(user)
    # else:
    #     post.like_users.add(user)
    if post.like_users.filter(pk=user.id).exists():
        post.like_users.remove(user)
    else:
        post.like_users.add(user)
    return redirect('posts:list')
    
@login_required
def comment_new(request, posts_pk):
    post = get_object_or_404(Post, pk=posts_pk)
    comment = Comment()
    comment.content = request.POST.get('content')
    comment.post = post
    comment.user = request.user
    comment.save()
    return redirect('posts:list')