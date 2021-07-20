from django.urls import path, include

from . import views

app_name = 'pets'

urlpatterns = [
    path('index', views.index, name='index'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('grooming', views.grooming, name='grooming'),
    #記帳
    path('bookkeeping', views.bookkeeping, name='bookkeeping'),
    path('bkupdate/<str:pk>', views.bkupdate, name='Bkupdate')
]
