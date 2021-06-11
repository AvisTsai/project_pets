"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
from pets.views import register

urlpatterns = [
    path(r'admin/', admin.site.urls),
    path(r'pets/', include('pets.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    # path(r'', admin.site.urls),
]

# def login(request):
#     return render(request, 'login.html')
#
# def register(request):
#     return render(request, 'register.html')
