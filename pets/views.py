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
            return redirect('pets:index')
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

# 散步
def walk(request):
    return render(request, 'pet-w0.html')
def walk1(request):
    return render(request, 'pet-w1.html')
def walk2(request):
    return render(request, 'pet-w2.html')
def walk3(request):
    return render(request, 'pet-w3.html')
def walk4(request):
    return render(request, 'pet-w4.html')
def walk5(request):
    return render(request, 'pet-w5.html')

def main(request):
    return render(request, 'main.html')

def login(request):
    return render(request, 'login.html')
def register(request):
    return render(request, 'register.html')
def index1(request):
    return render(request, 'index1.html')    

# 住宿
def consult(request):
    return render(request, 'pet-h.html')

# 美容
def grooming(request):
    return render(request, 'pet-g11.html')
def grooming1(request):
    return render(request, 'pet-g12.html')

# 訓練
def train(request):
    return render(request, 'pet-t11.html')
def train1(request):
    return render(request, 'pet-t12.html')

# 領養
def adopt(request):
    return render(request, 'pet-a.html')

def adopt1(request):
    return render(request, 'pet-a1.html')

def adopt2(request):
    return render(request, 'pet-a2.html')
    
def adopt3(request):
    return render(request, 'pet-a3.html')

def adopt4(request):
    return render(request, 'pet-a4.html')

def adopt5(request):
    return render(request, 'pet-a5.html')

def adopt6(request):
    return render(request, 'pet-a6.html')    

# 商城
def s11(request):
    return render(request, 'pet-s11.html')  
def s12(request):
    return render(request, 'pet-s12.html')  
def s13(request):
    return render(request, 'pet-s13.html')  

def s21(request):
    return render(request, 'pet-s21.html')  
def s22(request):
    return render(request, 'pet-s22.html')  
def s31(request):
    return render(request, 'pet-s31.html')  
def s32(request):
    return render(request, 'pet-s32.html')  
def s33(request):
    return render(request, 'pet-s33.html')  
def s34(request):
    return render(request, 'pet-s34.html')  
def s35(request):
    return render(request, 'pet-s35.html')  
def s36(request):
    return render(request, 'pet-s36.html')  
def s37(request):
    return render(request, 'pet-s37.html')  
def s38(request):
    return render(request, 'pet-s38.html')  
def s41(request):
    return render(request, 'pet-s41.html')  
def s42(request):
    return render(request, 'pet-s42.html')  
def s43(request):
    return render(request, 'pet-s43.html')  
def s44(request):
    return render(request, 'pet-s44.html')  

# 寵物醫院

# 諮詢
def line(request):
    return render(request, 'pet-h1.html')
# 看診
def h2(request):
    return render(request, 'pet-h2.html')
# 門診
def h3(request):
    return render(request, 'pet-h3.html')
# 健康
def h4(request):
    return render(request, 'pet-h4.html')
# 地圖
def h5(request):
    return render(request, 'pet-h5.html')
def h51(request):
    return render(request, 'pet-h51.html')
def h52(request):
    return render(request, 'pet-h52.html')
def h53(request):
    return render(request, 'pet-h53.html')
def h54(request):
    return render(request, 'pet-h54.html')
def h55(request):
    return render(request, 'pet-h55.html')

# 常見
def h6(request):
    return render(request, 'pet-h6.html')
# 關於
def h7(request):
    return render(request, 'pet-h7.html')

# 基本
def QA(request):
    return render(request, 'QA.html')
def pr(request):
    return render(request, 'privacy.html')