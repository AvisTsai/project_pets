from django.urls import path, include

from . import views
from django.conf.urls import url

app_name = 'pets'

urlpatterns = [
    path('index', views.index, name='index'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    
    # 散步
     path('walk/', views.walk, name='walk'),
     path('walk1/', views.walk1, name='walk1'),
     path('walk2/', views.walk2, name='walk2'),
     path('walk3/', views.walk3, name='walk3'),
     path('walk4/', views.walk4, name='walk4'),
     path('walk5/', views.walk5, name='walk5'),
    
    # 住宿
    path('consult', views.consult, name='consult'),

    # 美容
    path('grooming', views.grooming, name='grooming'),
    path('grooming1', views.grooming1, name='grooming1'),
    
    # 訓練
    path('train', views.train, name='train'),
    path('train1', views.train1, name='train1'),

    # 記帳
    path('bookkeeping/', views.bookkeeping, name='bookkeeping'),
    path('update/<str:pk>', views.update, name='update'),
    path('delete/<str:pk>', views.delete, name='delete'),

    # 行事曆
    path('calendar/', views.CalendarView.as_view(), name='calendar'),
    path('event/new/', views.event, name='event_new'),
    # path('event/edit/(?P<event_id>\d+)/', views.event, name='event_edit'),


    # 領養
    path('adopt', views.adopt, name="adopt"),
    path('adopt1', views.adopt1, name="adopt1"),
    path('adopt2', views.adopt2, name="adopt2"),
    path('adopt3', views.adopt3, name="adopt3"),
    path('adopt4', views.adopt4, name="adopt4"),
    path('adopt5', views.adopt5, name="adopt5"),
    path('adopt6', views.adopt6, name="adopt6"),
   
    # 諮詢
    path('line', views.line, name='line'),
    path('h2', views.h2, name='h2'),
    path('h3', views.h3, name='h3'),
    path('h4', views.h4, name='h4'),
    path('h5', views.h5, name='h5'),
    path('h51', views.h51, name='h51'),
    path('h52', views.h52, name='h52'),
    path('h53', views.h53, name='h53'),
    path('h54', views.h54, name='h54'),
    path('h55', views.h55, name='h55'),
    path('h6', views.h6, name='h6'),
    path('h7', views.h7, name='h7'),
    
    # 商城
    path('s11', views.s11, name='s11'),
    path('s12', views.s12, name='s12'),
    path('s13', views.s13, name='s13'),
    path('s21', views.s21, name='s21'),
    path('s22', views.s22, name='s22'),
    path('s31', views.s31, name='s31'),
    path('s32', views.s32, name='s32'),
    path('s33', views.s33, name='s33'),
    path('s34', views.s34, name='s34'),
    path('s35', views.s35, name='s35'),
    path('s36', views.s36, name='s36'),
    path('s37', views.s37, name='s37'),
    path('s38', views.s38, name='s38'),
    path('s41', views.s41, name='s41'),
    path('s42', views.s42, name='s42'),
    path('s43', views.s43, name='s43'),
    path('s44', views.s44, name='s44'),

    # 基本
    path('QA', views.QA, name='QA'),
    path('pr', views.pr, name='pr'),
    path('main', views.main, name='main'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('index1', views.index1, name='index1'),

]
