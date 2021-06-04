from django.shortcuts import render
from django.http import HttpResponse
from .models import Pet


def index(request):
    pets = Pet.objects.all()
    return render(request, 'pets/index.html', {'pets': pets})

# def index(request):
#     return HttpResponse('<h1>寵物</h1>')

