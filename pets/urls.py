from django.urls import path, include

from . import views

app_name = 'pets'

urlpatterns = [
    path('index', views.index, name='index'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('grooming', views.grooming, name='grooming'),
    # 記帳
    path('bookkeeping/', views.bookkeeping, name='bookkeeping'),
    path('update/<str:pk>', views.update, name='update'),
    path('delete/<str:pk>', views.delete, name='delete'),
    # 領養
    path('adopt', views.adopt, name="adopt"),
    path('adopt1', views.adopt1, name="adopt1"),
    # 住宿
    path('consult', views.consult, name='consult'),
    # 諮詢
    path('line', views.line, name='line'),
]
