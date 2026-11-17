from django.shortcuts import render, redirect, get_object_or_404
from .forms import FeedbackForm, CommentForm, BlogForm
from django.contrib.auth.forms import UserCreationForm
from .models import Blog, Comment

def home(request):
    return render(request, 'app/about.html', {
        'title': 'Онлайн-курсы'
    })


def links(request):
    return render(request, 'app/links.html', {
        'title': 'Полезные ссылки'
    })


def feedback(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)

        if form.is_valid():

            data = {
                'name': form.cleaned_data['name'],
                'email': form.cleaned_data['email'],
                'course': form.cleaned_data['course'],
                'rating': form.cleaned_data['rating'],
                'topics': form.cleaned_data['topics'],
                'wishes': form.cleaned_data['wishes'],
            }

            return render(request, 'app/pool.html', {
                'title': 'Обратная связь',
                'form': None,
                'data': data
            })

    else:
        form = FeedbackForm()

    return render(request, 'app/pool.html', {
        'title': 'Обратная связь',
        'form': form
    })

def registration(request):
    if request.method == 'POST':
        regform = UserCreationForm(request.POST)

        if regform.is_valid():
            user = regform.save()
            user.is_staff = False
            user.is_active = True
            user.is_superuser = True
            user.save()

            return redirect('home')
    else:
        regform = UserCreationForm()

    return render(request, 'app/registration.html', {
        'regform': regform,
        'title': 'Регистрация'
    })

def blog(request):
    posts = Blog.objects.all().order_by('-posted')
    return render(request, 'app/blog.html', {
        'title': 'Блог',
        'posts': posts
    })

def blogpost(request, parameter):
    post = get_object_or_404(Blog, id=parameter)
    comments = Comment.objects.filter(post=post).order_by('-date')
    if request.method == 'POST':
        if request.user.is_authenticated:
            form = CommentForm(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.author = request.user
                comment.post = post
                comment.save()
                return redirect('blogpost', parameter=post.id)
        else:
            form = CommentForm()
    else:
        form = CommentForm()

    return render(request, 'app/blogpost.html', {
        'title': post.title,
        'post': post,
        'comments': comments,
        'form': form
    })

def newpost(request):
    if not request.user.is_superuser:
        return redirect('blog')

    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)

        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()

            return redirect('blog')
    else:
        form = BlogForm()

    return render(request, 'app/newpost.html', {
        'form': form,
        'title': 'Добавление статьи'
    })

def videopost(request):
    return render(request, 'app/videopost.html', {
        'title': 'Видео'
    })