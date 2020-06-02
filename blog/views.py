from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post

def home(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, "home.html", context)

class PostListView(ListView):
    model = Post
    template_name = 'home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']

class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'

def about(request):
    context = {}
    return render(request, "about.html", context)
