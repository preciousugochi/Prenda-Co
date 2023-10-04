from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages
from .models import Feature
# Create your views here.

def index(request):
    features = Feature.objects.all()
    
    return render(request, 'index.html', {'features': features})

def counter(request):
    posts = [1, 2, 3, 4, 5, 'tim', 'tom', 'ugo']
    return render(request, 'counter.html', {'posts': posts})

def static(request):
    return render(request, 'static.html')

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username', True)
        email = request.POST.get('email', False)
        password = request.POST.get('password', False)
        password2 = request.POST.get('password2', False)

        if password==password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email already used')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username Already Exists')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                return redirect('login')
        else:
            messages.info(request, 'Password not the same')
            return redirect('register')
        
    else:
        return render(request, 'register.html')

def login(request):
    if request.method =='POST':
        username = request.POST.get('username', True)
        password = request.POST.get('password', False)

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Credentials invalid')
            return redirect('login')
    else:
        return render(request, 'login.html')
    
def logout(request):
    #logs out an authenticated user
    auth.logout(request)
    #redirects to home page
    return redirect('/')

def post(request, pk):
    return render(request, 'post.html', {'pk': pk})
