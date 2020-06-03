from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from blog.models import Post
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from .models import Profile

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Welcome {username} 👋! You may login now!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    context = {'form': form}
    return render(request, "register.html", context)

@login_required
def profile_edit(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if p_form.is_valid() and u_form.is_valid():
            p_form.save()
            u_form.save()
            messages.success(request, 'Hey ✋! Your details have been updated!')
            return redirect('profile')
    else:   
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, "profile_edit.html", context)

class ProfileListView(LoginRequiredMixin, ListView):
    model = Post
    paginate_by = 2
    template_name = 'profile.html'
    context_object_name = 'posts'

    def get_queryset(self):
        _user = get_object_or_404(User, id=self.request.user.id)
        return Post.objects.filter(author=_user).all().order_by('-date_posted')

class ProfileIdListView(ListView):
    model = Post
    paginate_by = 2
    template_name = 'profile_id.html'
    context_object_name = 'posts'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile_user'] = User.objects.filter(username=self.kwargs['username']).first()
        return context

    def get_queryset(self):
        user_id = get_object_or_404(User, username=self.kwargs.get('username'))  
        return Post.objects.filter(author=user_id).all().order_by('-date_posted')
