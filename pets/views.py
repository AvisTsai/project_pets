import datetime

from django.contrib.auth import authenticate
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import auth
from .forms import RegisterForm, MoneyForm
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from .models import Money


def index(request):
    return render(request, 'index.html')


# 註冊
@csrf_exempt
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pets:login')
        else:
            return redirect('pets:register')
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
            return redirect('pets:login')
        elif user and user.is_staff is True:
            auth.login(request, user)
            return redirect('/pets')
        else:
            return redirect('pets:login')
    else:
        return render(request, 'login.html', locals())


def logout(request):
    auth.logout(request)
    return redirect('/index')


def grooming(request):
    return render(request, 'pet-g11.html', locals())


# 記帳
def current_time(request):
    now = datetime.datetime.now()
    time_style = now.strftime("%Y-%m-%d %H:%M:%S")
    return render(request, 'pet-m.html', {'cur_time': time_style})


def bookkeeping(request):
    money = Money.objects.all()  # 查詢所有資料
    form = MoneyForm()
    if request.method == 'POST':
        form = MoneyForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("pets:bookkeeping")

    context = {
        'money': money,
        'form': MoneyForm
    }

    return render(request, 'pet-m.html', context)


def update(request, pk):
    money = Money.objects.get(id=pk)
    form = MoneyForm(instance=money)

    if request.method == 'POST':
        form = MoneyForm(request.POST, instance=money)
        if form.is_valid():
            form.save()
        return redirect("pets:bookkeeping")

    context = {
        'form': form

    }

    return render(request, 'update.html', context)


def delete(request, pk):
    money = Money.objects.get(id=pk)

    if request.method == "POST":
        money.delete()
        return redirect('pets:bookkeeping')

    context = {
        'money': money
    }

    return render(request, 'delete.html', context)
