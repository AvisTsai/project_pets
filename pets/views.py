import datetime

from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib import auth
from .forms import RegisterForm, MoneyForm, EventForm
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, CreateView, UpdateView
from datetime import datetime, timedelta, date
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.urls import reverse, reverse_lazy
from django.utils.safestring import mark_safe
import calendar
from django.contrib.auth.forms import UserCreationForm

from .models import *
from .utils import Calendar


def index(request):
    return render(request, 'index.html')


# 註冊
def registerweb(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pets:login')
        else:
            return render(request, 'registerweb.html', {'form': form})
    else:
        form = RegisterForm()
        context = {'form': form}
        return render(request, 'registerweb.html', context)


def login(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('pets:index')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)

        if user is not None and user.is_active:
            auth.login(request, user)
            return redirect('pets:index')
        else:
            return HttpResponse('使用者名稱或密碼錯誤')

    return render(request, 'login.html', locals())


def logout(request):
    auth.logout(request)
    return redirect('/index')


def grooming(request):
    return render(request, 'grooming_pet.html', locals())


# 記帳
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

    return render(request, 'bookkeeping.html', context)


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


# 行事曆
class CalendarView(generic.ListView):
    model = Event
    template_name = 'calendar.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # use today's date for the calendar
        d = get_date(self.request.GET.get('month', None))

        # Instantiate our calendar class with today's year and date
        cal = Calendar(d.year, d.month)

        # Call the formatmonth method, which returns our calendar as a table
        html_cal = cal.formatmonth(withyear=True)
        context['calendar'] = mark_safe(html_cal)
        context['prev_month'] = prev_month(d)
        context['next_month'] = next_month(d)
        return context


def prev_month(d):
    first = d.replace(day=1)
    print('first', first)
    prev_month = first - timedelta(days=1)
    print(prev_month)
    month = 'month=' + str(prev_month.year) + '-' + str(prev_month.month)
    return month


def next_month(d):
    days_in_month = calendar.monthrange(d.year, d.month)[1]
    # print('days_in_month', days_in_month)
    # 31
    last = d.replace(day=days_in_month)
    # print('last', last)
    # 2021-12-31
    next_month = last + timedelta(days=1)
    # print(next_month)
    # 2022-01-01
    month = 'month=' + str(next_month.year) + '-' + str(next_month.month)
    # print(month)
    # mouth=2022-1
    return month


def get_date(req_day):
    if req_day:
        year, month = (int(x) for x in req_day.split('-'))
        return date(year, month, day=1)
    return datetime.today()


def event(request, event_id=None):
    instance = Event()
    if event_id:
        instance = get_object_or_404(Event, pk=event_id)
    else:
        instance = Event()

    form = EventForm(request.POST or None, instance=instance)
    if request.POST and form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('pets:calendar'))
    return render(request, 'event.html', {'form': form})


# 刪除事件
def delEvent(request, event_id=None):
    instance = Event.objects.get(id=id)
    instance.delete()
    return render(request, 'delEvent.html')


# 行事曆搜尋功能
def titleSearch(request):
    q = request.GET.get('q')

    if not q:
        error_msg = '请输入关键词'
        return render(request, 'result.html', {'error_msg': error_msg})
    title = Event.objects.filter(title__icontains=q)
    return render(request, 'result.html', {'title': title})


# titleSearch()

def viewTitle(request):
    # t = Calendar.getEventurl(events)
    title = Event.objects.order_by('start_time')
    # title.order_by("start_time")
    # description = Event.objects.all()

    context = {'title': title}

    return render(request, 'Calendar_title.html', context)


# 散步
def walk_pet(request):
    return render(request, 'walk_pet.html')


def walk_Taipei(request):
    return render(request, 'walk_Taipei.html')


def walk_Taoyuan(request):
    return render(request, 'walk_Taoyuan.html')


def walk_Taizhong(request):
    return render(request, 'walk_Taizhong.html')


def walk_Tainan(request):
    return render(request, 'walk_Tainan.html')


def walk_Kaohsiung(request):
    return render(request, 'walk_Kaohsiung.html')


# 基本

def main(request):
    return render(request, 'main.html')


def login(request):
    return render(request, 'login.html')

def forgot(request):
    return render(request, 'forgot.html')


def register(request):
    return render(request, 'registerweb.html')


def index1(request):
    return render(request, 'index1.html')


# 住宿
def consult(request):
    return render(request, 'consult.html')


# 美容
def grooming_pet(request):
    return render(request, 'grooming_pet.html')


def grooming_find(request):
    return render(request, 'grooming_find.html')


# 訓練
def train_pet(request):
    return render(request, 'train_pet.html')


def train_find(request):
    return render(request, 'train_find.html')


# 領養
def adopt_pet1(request):
    return render(request, 'adopt_pet1.html')


def adopt_pet2(request):
    return render(request, 'adopt_pet2.html')


def adopt_pet3(request):
    return render(request, 'adopt_pet3.html')


def adopt_pet4(request):
    return render(request, 'adopt_pet4.html')


def adopt_pet5(request):
    return render(request, 'adopt_pet5.html')


def adopt_pet6(request):
    return render(request, 'adopt_pet6.html')


def adopt_pet7(request):
    return render(request, 'adopt_pet7.html')


# 商城
def mall_freshfood1(request):
    return render(request, 'mall_freshfood1.html')


def mall_freshfood2(request):
    return render(request, 'mall_freshfood2.html')


def mall_freshfood3(request):
    return render(request, 'mall_freshfood3.html')


def mall_feed1(request):
    return render(request, 'mall_feed1.html')


def mall_feed2(request):
    return render(request, 'mall_feed2.html')


def mall_clothing1(request):
    return render(request, 'mall_clothing1.html')


def mall_clothing2(request):
    return render(request, 'mall_clothing2.html')


def mall_clothing3(request):
    return render(request, 'mall_clothing3.html')


def mall_clothing4(request):
    return render(request, 'mall_clothing4.html')


def mall_clothing5(request):
    return render(request, 'mall_clothing5.html')


def mall_clothing6(request):
    return render(request, 'mall_clothing6.html')


def mall_clothing7(request):
    return render(request, 'mall_clothing7.html')


def mall_clothing8(request):
    return render(request, 'mall_clothing8.html')


def mall_accessories1(request):
    return render(request, 'mall_accessories1.html')


def mall_accessories2(request):
    return render(request, 'mall_accessories2.html')


def mall_accessories3(request):
    return render(request, 'mall_accessories3.html')


def mall_accessories4(request):
    return render(request, 'mall_accessories4.html')


# 寵物醫院


# 看診
def Hospital_visits(request):
    return render(request, 'Hospital_visits.html')


# 健康
def Hospital_healthcheck(request):
    return render(request, 'Hospital_healthcheck.html')


# 地圖
def Hospital_map(request):
    return render(request, 'Hospital_map.html')


def Hospital_mapTPE(request):
    return render(request, 'Hospital_mapTPE.html')


def Hospital_mapTYC(request):
    return render(request, 'Hospital_mapTYC.html')


def Hospital_mapTXG(request):
    return render(request, 'Hospital_mapTXG.html')


def Hospital_mapTNN(request):
    return render(request, 'Hospital_mapTNN.html')


def Hospital_mapKHH(request):
    return render(request, 'Hospital_mapKHH.html')


# 葬儀
def funeral_pet(request):
    return render(request, 'funeral_pet.html')


def funeral_find(request):
    return render(request, 'funeral_find.html')


# 常見
def Hospital_commonproblem(request):
    return render(request, 'Hospital_commonproblem.html')


# 關於
def aboutus(request):
    return render(request, 'aboutus.html')


# 基本
def QA(request):
    return render(request, 'QA.html')


def privacy(request):
    return render(request, 'privacy.html')
