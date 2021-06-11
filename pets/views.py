from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm


def index(request):
    # pets = Pet.objects.all()
    # return render(request, 'pets/index.html', {'pets': pets})
    return render(request, 'web/index.html')


# 註冊
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        print("Errors", form.errors)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('web/register.html')
        else:
            return render(request, 'web/register.html',
    {'form': form})
    else:
        form = UserCreationForm()
        context = {'form': form}
        return render(request, 'web/register.html', context)


# def add(request):
#     form = PetForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         messages.success(request, '新增成功')
#         return redirect('pets:index')
#     return render(request, 'pets/add.html', {'form': form})
