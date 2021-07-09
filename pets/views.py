from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.contrib import auth
from .forms import RegisterForm
from django.views.decorators.csrf import csrf_exempt


def index(request):
    # pets = Pet.objects.all()
    # return render(request, 'pets/index.html', {'pets': pets})
    return render(request, 'index.html')


# 註冊
@csrf_exempt
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login')
        else:
            return redirect('/register')
    context = {
        'form': RegisterForm
    }

    return render(request, 'register.html', context)


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user and user.is_staff is False:
            auth.login(request, user)
            return redirect('/login')
        elif user and user.is_staff is True:
            auth.login(request, user)
            return redirect('/pets')
        else:
            return redirect('/login')
    else:
        return render(request, 'login.html', locals())


def logout(request):
    auth.logout(request)
    return redirect('index')
