from django.shortcuts import render
from .models import Post

def home(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, "home.html", context)

def about(request):
    context = {}
    return render(request, "about.html", context)