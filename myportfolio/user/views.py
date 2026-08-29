from django.shortcuts import HttpResponse ,render, redirect
from django.contrib.auth import authenticate, login
from django.urls import reverse
from .forms import RegisterForm

# Create your views here.

def index(request):
    print('-'*80)
    print(request.user.is_authenticated)
    print(request.user.is_superuser)
    print(request.user.is_staff)
    return render(request, 'user/profile.html')


def login(request, url):
    return render(request, 'user/login.html')

def logout(request):
    redirect('')

def register(request):
   form = RegisterForm()
   if request.method == 'POST':
       form = RegisterForm(request.POST)
       if form.is_valid():
           form.save()
           username = form.cleaned_data.get('username')
           password = form.cleaned_data.get('password1')
           user = authenticate(username=username, password=password)
           login(request, user)  # 로그인
           return redirect(reverse('user:login'))
   return render(request, 'user/register.html', {'form': form})

