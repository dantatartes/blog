from django.shortcuts import render, get_object_or_404
from .models import Post


def home(request):
    all_posts = Post.post_manager.all()
    return render(request, "home.html", {'posts': all_posts})


def post_full(request, post):
    post = get_object_or_404(Post, slug=post, status='published')
    return render(request, 'post_full.html', {'post': post})
