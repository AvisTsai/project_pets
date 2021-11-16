from django.urls import path, include

from . import views
from django.conf.urls import url

app_name = 'pets'

urlpatterns = [
    path('index', views.index, name='index'),
    path('registerweb', views.registerweb, name='registerweb'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('aboutus', views.aboutus, name='aboutus'),
    path('forgot', views.forgot, name='forgot'),
    path('registerweb', views.registerweb, name='registerweb'),
    # 散步
     path('walk_pet', views.walk_pet, name='walk_pet'),
     path('walk_Taipei', views.walk_Taipei, name='walk_Taipei'),
     path('walk_Taoyuan', views.walk_Taoyuan, name='walk_Taoyuan'),
     path('walk_Taizhong', views.walk_Taizhong, name='walk_Taizhong'),
     path('walk_Tainan', views.walk_Tainan, name='walk_Tainan'),
     path('walk_Kaohsiung', views.walk_Kaohsiung, name='walk_Kaohsiung'),
    
    # 住宿
    path('consult', views.consult, name='consult'),

    # 美容
    path('grooming_pet', views.grooming_pet, name='grooming_pet'),
    path('grooming_find', views.grooming_find, name='grooming_find'),
    
    # 訓練
    path('train_pet', views.train_pet, name='train_pet'),
    path('train_find', views.train_find, name='train_find'),

    # 記帳
    path('bookkeeping/', views.bookkeeping, name='bookkeeping'),
    path('update/<str:pk>', views.update, name='update'),
    path('delete/<str:pk>', views.delete, name='delete'),

    # 行事曆  path(URL路徑，views的def,方便管理的名稱
    path('calendar', views.CalendarView.as_view(), name='calendar'),
    #path('calendar', views.viewTitle, name='calendar'),
    path('event/new/', views.event, name='event_new'),
    path('CalTitle/', views.viewTitle, name='CalTitle'),
    path('event/edit/<str:event_id>/', views.event, name='event_edit'),
    path('result/', views.titleSearch, name='result'),
    path('delEvent/<event_id>', views.delEvent, name='deleteEvent'),



    # 領養
    path('adopt_pet1', views.adopt_pet1, name="adopt_pet1"),
    path('adopt_pet2', views.adopt_pet2, name="adopt_pet2"),
    path('adopt_pet3', views.adopt_pet3, name="adopt_pet3"),
    path('adopt_pet4', views.adopt_pet4, name="adopt_pet4"),
    path('adopt_pet5', views.adopt_pet5, name="adopt_pet5"),
    path('adopt_pet6', views.adopt_pet6, name="adopt_pet6"),
    path('adopt_pet7', views.adopt_pet7, name="adopt_pet7"),
   
   

    # 寵物醫院
    path('Hospital_visits', views.Hospital_visits, name='Hospital_visits'),
    path('Hospital_healthcheck', views.Hospital_healthcheck, name='Hospital_healthcheck'),
    path('Hospital_map', views.Hospital_map, name='Hospital_map'),
    path('Hospital_mapTPE', views.Hospital_mapTPE, name='Hospital_mapTPE'),
    path('Hospital_mapTYC', views.Hospital_mapTYC, name='Hospital_mapTYC'),
    path('Hospital_mapTXG', views.Hospital_mapTXG, name='Hospital_mapTXG'),
    path('Hospital_mapTNN', views.Hospital_mapTNN, name='Hospital_mapTNN'),
    path('Hospital_mapKHH', views.Hospital_mapKHH, name='Hospital_mapKHH'),
    path('Hospital_commonproblem', views.Hospital_commonproblem, name='Hospital_commonproblem'),
    path('funeral_pet', views.funeral_pet, name='funeral_pet'),
    path('funeral_find', views.funeral_find, name='funeral_find'),


    
    # 商城
    path('mall_freshfood1', views.mall_freshfood1, name='mall_freshfood1'),
    path('mall_freshfood2', views.mall_freshfood2, name='mall_freshfood2'),
    path('mall_freshfood3', views.mall_freshfood3, name='mall_freshfood3'),
    path('mall_feed1', views.mall_feed1, name='mall_feed1'),
    path('mall_feed2', views.mall_feed2, name='mall_feed2'),
    path('mall_clothing1', views.mall_clothing1, name='mall_clothing1'),
    path('mall_clothing2', views.mall_clothing2, name='mall_clothing2'),
    path('mall_clothing3', views.mall_clothing3, name='mall_clothing3'),
    path('mall_clothing4', views.mall_clothing4, name='mall_clothing4'),
    path('mall_clothing5', views.mall_clothing5, name='mall_clothing5'),
    path('mall_clothing6', views.mall_clothing6, name='mall_clothing6'),
    path('mall_clothing7', views.mall_clothing7, name='mall_clothing7'),
    path('mall_clothing8', views.mall_clothing8, name='mall_clothing8'),
    path('mall_accessories1', views.mall_accessories1, name='mall_accessories1'),
    path('mall_accessories2', views.mall_accessories2, name='mall_accessories2'),
    path('mall_accessories3', views.mall_accessories3, name='mall_accessories3'),
    path('mall_accessories4', views.mall_accessories4, name='mall_accessories4'),

    # 基本
    path('QA', views.QA, name='QA'),
    path('privacy', views.privacy, name='privacy'),
    path('main', views.main, name='main'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('index1', views.index1, name='index1'),

]
