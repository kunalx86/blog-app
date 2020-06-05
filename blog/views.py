from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.http import JsonResponse, HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Comment
from .forms import CommentCreateForm

class PostListView(ListView):
    model = Post
    template_name = 'home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 2

class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            context['comment_form'] = CommentCreateForm()
        context['comments'] = Comment.objects.filter(post=context['object'].id, parent=None).all().order_by('-date_posted')
        return context

    def post(self, request, pk, *args, **kwargs):
        self.object = self.get_object()
        comment_form = CommentCreateForm(request.POST or None)
        if comment_form.is_valid():
            body = request.POST.get('body')
            post = Post.objects.filter(id=pk).first()
            reply_id = request.POST.get('comment_id')
            comment_qs = None
            if reply_id:
                comment_qs = Comment.objects.get(id=reply_id)
            comment = Comment.objects.create(body=body, author=self.request.user, post=post, parent=comment_qs)
            comment.save()
            if self.request.is_ajax():
                html = render_to_string('comments.html', self.get_context_data(**kwargs), request=self.request)
                return JsonResponse({'html': html})
            return redirect("post-detail", pk=pk)

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'post_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'post_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'post_confirm_delete.html'
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

def get_comments(request):
    post_id = request.GET.get('post_id', None)
    comments = list(Comment.objects.filter(post=post_id).all().order_by('-date_posted').values())
    return JsonResponse({'comments': comments}, safe=False)

def about(request):
    context = {}
    return render(request, "about.html", context)
