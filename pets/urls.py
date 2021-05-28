from django.urls import path
from . import views

app_name = 'pets'
urlpatterns = [
    path('', views.index, name='index'),
    # path(r'^register/', views.register, name='register'),
    # path(r'^login/', views.login, name='login'),
]