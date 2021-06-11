from django.urls import path, include

from . import views
from .views import register

app_name = 'pets'


urlpatterns = [
    path('', views.index),
    path('register', views.register, name='register'),
    # path(r'^login/', views.login, name='login'),
]