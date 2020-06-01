from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm
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
def profile(request):
    user = request.user
    profile = Profile.objects.filter(user=user).first()
    context = {}
    return render(request, "profile.html", context)