from django.shortcuts import render
from .models import Post


def home(request):
    all_posts = Post.post_manager.all()
    return render(request, "home.html", {'posts': all_posts})
