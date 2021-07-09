from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
import tkinter as tk
from tkinter import ttk
from datetime import *
import calendar
from django.shortcuts import render
from bs4 import BeautifulSoup
import requests

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

#行事曆顯示月份

def displayMouth(request):
    url = "https://www.maxlist.xyz/"
    res = requests.get(url)
    soup = BeautifulSoup(res.text,"html.parser")
    title = soup.select('title')
    return render(request,'project_pets/templates/web/calendar.html',locals())
    '''
    todayy  = date.today()
    de_y = todayy.year
    de_m = todayy.month
#print(de_y,de_m)
    app = tk.Tk() 
    app.geometry('500x300')
    text_cal = calendar.TextCalendar(firstweekday = 0) 
    labelYear = tk.Label(text = "請输入年份")
    labelYear.grid(column=0, row=0, sticky=tk.W)
    labelCity = tk.Label(text = "請输入月份")
    labelCity.grid(column=0, row=1, sticky=tk.W)
    pic_1 = tk.PhotoImage(file='icons8-forward-16.png')
    pic_2 = tk.PhotoImage(file='icons8-back-16.png')

    YearString = tk.StringVar()
    YearString.set(de_y)
    MouthString = tk.StringVar()
    MouthString.set(de_m)
    def YearAdd():
        i = entryY.get()
        p = int(i) + 1
        YearString.set(str(p))
    def YearReduce():
        i = entryY.get()
        p = int(i) - 1
        YearString.set(str(p))
    btn_YA = tk.Button(image=pic_1,command=YearAdd)
    btn_YA.grid(column=3, row=0, pady=10, sticky=tk.W)
    btn_YR = tk.Button(image=pic_2,command=YearReduce)
    btn_YR.grid(column=2, row=0, pady=10, sticky=tk.W)
    entryY = tk.Entry(width=20, textvariable=YearString)
    entryM = tk.Entry(width=20, textvariable=MouthString)
    entryY.grid(column=1, row=0, padx=10)
    entryM.grid(column=1, row=1, padx=10)
    def MAdd():
        i = entryM.get()
        p = int(i) + 1
        MouthString.set(str(p))
    def MReduce():
        i = entryM.get()
        p = int(i) - 1
        MouthString.set(str(p))

    btn_YA = tk.Button(image=pic_1,command=MAdd)
    btn_YA.grid(column=3, row=1, pady=10, sticky=tk.W)
    btn_YR = tk.Button(image=pic_2,command=MReduce)
    btn_YR.grid(column=2, row=1, pady=10, sticky=tk.W)


    def callbackFunc():
        resultString.set("{}/{}".format(YearString.get(),
                                        MouthString.get()))
        resultLabe3 = tk.Label(text=str(text_cal.formatmonth(int(YearString.get()),
                                        int(MouthString.get()),w=5)))
        resultLabe3.place(relx = 0.5, rely = 0.5, anchor = "CENTER")
        
    resultButton = tk.Button(app, text = 'OK',
                            command=callbackFunc)

    resultButton.grid(column=0, row=2, pady=10, sticky=tk.W)

    resultString=tk.StringVar()
    resultLabel = tk.Label(app, textvariable=resultString)
    resultLabel.grid(column=1, row=2, padx=10, sticky=tk.W)
    calendarYM = resultString
    app.mainloop()'''

