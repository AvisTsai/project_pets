'''import pandas as pd
 
df = pd.read_excel("日曆.xlsx", sheet_name="11月")
print(df)

import xlrd
data=xlrd.open_workbook(r"日曆.xlsx")
'''
'''import openpyxl
f = openpyxl.load_workbook('日曆2.xlsx')
table = f['9月']
print(table)'''

'''import pandas as pd
df = pd.read_excel(r'日曆2.xlsx',sheet_name = '9月')

collist = df.columns

for i in range(df.shape[1]):
    #for loop col
    for j in range(df.shape[1]):
        item = df.iloc[j,j]
        print('row:',i,'/col:',j,'/',item)'''

'''
import tkinter as tk

def createNewWindow():
    newWindow = tk.Toplevel(app)
    labelExample = tk.Label(newWindow, text = "New Window")
    buttonExample = tk.Button(newWindow, text = "New Window button")

    labelExample.pack()
    buttonExample.pack()

app = tk.Tk()
buttonExample = tk.Button(app, 
              text="Create new window",
              command=createNewWindow)
buttonExample.pack()

app.mainloop()'''


import tkinter as tk
import calendar
window = tk.Tk()
window.title('window')
window.geometry('500x300')
#lbl_1 = tk.Label(window, text='Hello World', bg='yellow', fg='#263238', font=('Arial', 12))
#lbl_1.grid(column=0, row=0)

lbl_1 = tk.Label(window, text='請输入年份:', bg='yellow', fg='#263238', font=('Arial', 12))
lbl_2 = tk.Label(window, text='請输入月份:', bg='yellow', fg='#263238', font=('Arial', 12))
lbl_1.pack()
lbl_2.pack()
en_1 = tk.Entry()
# 输入指定年月
yy = int(input("請输入年份: "))
mm = int(input("输入月份: "))

# 显示日历
print(calendar.month(yy,mm))
window.mainloop()