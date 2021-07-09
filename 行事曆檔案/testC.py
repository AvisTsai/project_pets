import tkinter as tk
from tkinter import ttk
from datetime import *
import calendar
import numpy as np
from tkinter import ttk
from tkinter import *

todayy = date.today()
de_y = todayy.year
de_m = todayy.month
# print(de_y,de_m)
app = tk.Tk()
#app.geometry('500x300')
text_cal = calendar.TextCalendar(firstweekday=0)
labelYear = tk.Label(text="請输入年份:")
labelYear.grid(column=0, row=0, sticky=tk.W)
labelCity = tk.Label(text="請输入月份:")
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

btn_YA = tk.Button(image=pic_1, command=YearAdd)
btn_YA.grid(column=3, row=0, pady=10, sticky=tk.W)
btn_YR = tk.Button(image=pic_2, command=YearReduce)
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

btn_YA = tk.Button(image=pic_1, command=MAdd)
btn_YA.grid(column=3, row=1, pady=10, sticky=tk.W)
btn_YR = tk.Button(image=pic_2, command=MReduce)
btn_YR.grid(column=2, row=1, pady=10, sticky=tk.W)

# def callbackFunc():
#     resultString.set("{}/{}".format(YearString.get(),
#                                         MouthString.get()))
#     resultLabe3 = tk.Label(text=str(text_cal.formatmonth(int(YearString.get()),
#                                         int(MouthString.get()), w=5)))
#     resultLabe3.place(relx=0.5, rely=0.5)

#一格一格
def squMouth():
    Weeklist= ("Sun","Mon","Tue","Wed","Thu","Fri","Sat")
    columns = Weeklist
    calendar.setfirstweekday(firstweekday=6)
    treeview = ttk.Treeview(app, height=18, show="headings", columns=columns)  # 表格

    for i in Weeklist:
        treeview.column(i, width=100, anchor='center')
        treeview.heading(i, text=i) 
    
    treeview.grid(column=3, row=4, pady=10)

    datalist = []
    for j in range(len(calendar.monthcalendar(int(YearString.get()),
                                            int(MouthString.get())))):
        for k in range(len(calendar.monthcalendar(int(YearString.get()),
                                            int(MouthString.get()))[j])):
            value = calendar.monthcalendar(int(YearString.get()),
                                            int(MouthString.get()))[j][k] # 將0值變為空值
            if value == 0:
                value = '-' 
                datalist.append(value)
                #sheet.cell(row=j + 9, column=k + 1).value = value
                #tree.insert("",3,text="line1" ,values=("1","2","3")) 
                #treeview.insert('', "end", values = value)
            else:
                #treeview.insert('', "end", values = value)
                datalist.append(value)

    newlist = np.reshape(datalist, (5, 7))
    for i in range(0,5):
        listi = tuple(newlist[i])
        treeview.insert('', "end", values = listi)

resultButton = tk.Button(app, text='OK',
                             command=squMouth)

resultButton.grid(column=0, row=2, pady=10, sticky=tk.W)

resultString = tk.StringVar()
resultLabel = tk.Label(app, textvariable=resultString)
resultLabel.grid(column=1, row=2, padx=10, sticky=tk.W)
calendarYM = resultString

app.bind("<Escape>", lambda x: app.destroy())
app.mainloop()
