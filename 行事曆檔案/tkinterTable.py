
'''import tkinter
from  tkinter import ttk  #匯入內部包

win=tkinter.Tk()
tree=ttk.Treeview(win)#表格
tree["columns"]=("姓名","年齡","身高")
tree.column("姓名",width=100)   #表示列,不顯示
tree.column("年齡",width=100)
tree.column("身高",width=100)

tree.heading("姓名",text="姓名-name")  #顯示錶頭
tree.heading("年齡",text="年齡-age")
tree.heading("身高",text="身高-tall")

tree.insert("",0,text="line1" ,values=("1","2","3")) #插入資料，
tree.insert("",1,text="line1" ,values=("1","2","3"))
tree.insert("",2,text="line1" ,values=("1","2","3"))
tree.insert("",3,text="line1" ,values=("1","2","3"))

tree.pack()
win.bind("<Escape>", lambda x: win.destroy())
win.mainloop()
'''
'''
from tkinter import ttk
from tkinter import *
root = Tk()  # 初始框的声明
columns = ("姓名", "IP地址")
treeview = ttk.Treeview(root, height=18, show="headings", columns=columns)  # 表格
 
treeview.column("姓名", width=100, anchor='center') # 表示列,不显示
treeview.column("IP地址", width=300, anchor='center')
 
treeview.heading("姓名", text="姓名") # 显示表头
treeview.heading("IP地址", text="IP地址")
 
treeview.pack(side=LEFT, fill=BOTH)
 
name = ['电脑1','服务器','笔记本']
ipcode = ['10.13.71.223','10.25.61.186','10.25.11.163']
for i in range(min(len(name),len(ipcode))): # 写入数据
    treeview.insert('', i, values=(name[i], ipcode[i]))

root.mainloop()  # 进入消息循环
'''


# 練習月曆
import calendar
from tkinter import ttk
from tkinter import *
import numpy as np
from tkinter import messagebox
root = Tk()  # 初始框的声明
Weeklist = ("sun", "mon", "tue", "wed", "thu", "fri", "sat")
columns = Weeklist
calendar.setfirstweekday(firstweekday=6)
treeview = ttk.Treeview(
    root, height=8, show="headings", columns=columns)  # 表格

for i in Weeklist:
    treeview.column(i, width=100, anchor='center')
    treeview.heading(i, text=i)

treeview.pack(side=LEFT, fill=BOTH)

datalist = []
# 將當月日期存到datalist
for j in range(len(calendar.monthcalendar(2021, 7))):
    for k in range(len(calendar.monthcalendar(2021, 7)[j])):
        value = calendar.monthcalendar(2021, 7)[j][k]  # 將0值變為空值
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

# for i in range(1,6):
#     data = tuple(newlist[i-1]
#     for j in range(newlist[i-1]):
#         treeview.insert('', "end", values = data)
for i in range(1, 6):
    data = tuple(newlist[i-1])
    treeview.insert('', "end", values=data)

# btn_YA = ttk.Button(root,text = '新增事件或提醒', width=20, command='newEvent')
# btn_YA.pack()
# 雙擊進入編輯


def set_cell_value(event):  # 雙擊進入編輯
    for item in treeview.selection():
        #item = I001
        item_text = treeview.item(item, "values")
        # print(item_text)  # 輸出所選行的值
    # label_topic = ttk.Label(text="請输入事件名稱:")
    # label_topic.pack(pady=20)
    # label_remind = ttk.Label(text="請输入月份:")
    # label_remind.pack(pady=20)

    # topic_box = Entry()
    # topic_box.grid(row = 3,column = 8)
    # topic_box.pack()
    # remind_box = Entry()
    # remind_box.pack()

    column = treeview.identify_column(event.x)  # 列
    row = treeview.identify_row(event.y)  # 行
    # print(column,row)
    cn = int(str(column).replace('#', ''))
    rn = int(str(row).replace('I', ''))
    # print(cn, rn)
    # entryedit = Text(root, width=5+(cn-1)*5, height=1)
    # entryedit.place(x=16+(cn-1)*130, y=6+rn*20)
    # print(newlist[cn][rn-2])
    #print(item_text[cn-1])
    # Label_y = ttk.Label(text= '2021/7')
    # Label_y.pack()
    lable_date = ttk.Label(text = '您選擇的日期是:'+item_text[cn-1]+ '號',font=25)
    lable_date.pack(pady=10)

    #清除資料
    def reset():
        lable_date.destroy()
        reset_button.destroy()
        okb.destroy()

    # return cn-1
    def saveedit():
        # treeview.set(item, column=column, value=entryedit.get(0.0, "end"))
        # entryedit.destroy()
        okb.destroy()
        reset_button.destroy()
        if len(topic_box.get()) == 0:
            messagebox.showinfo("Error", "事件名稱未填寫")
            return

        lable_resu = ttk.Label(text='事件名稱 : ')
        lable_resu.pack(pady=10)
        lable_result = ttk.Label(text=topic_box.get())
        lable_result.pack(pady=10)
        lable_rsm = ttk.Label(text= str(hon_scale.get())+'小時前提醒。')
        lable_rsm.pack(pady=10)

        def saveEvent():
            data=open("output0709.txt",'w+') 
            lines = ['日期:\n', '2021/07/'+str(item_text[cn-1]), '事件名稱:\n', '小時前提醒\n']
            data.writelines(lines)
            data.close()

        #儲存
        save_button = ttk.Button(root, text='儲存', width=4, command=saveEvent)    
        save_button.pack(pady=20) 

    reset_button = ttk.Button(root, text='重設', width=4, command=reset)    
    reset_button.pack(pady=20) 
    okb = ttk.Button(root, text='OK', width=4, command=saveedit)
    # okb.place(x=50+(cn-1)*130,y=3+rn*25)
    okb.pack(pady=0)




label_topic = ttk.Label(text="請输入事件名稱:")
label_topic.pack(pady=20)
topic_box = Entry()
topic_box.pack()
#什麼時候提醒
label_remind = ttk.Label(text="請输入要什麼時候提醒您:")
label_remind.pack(pady=20)
hon_scale = Entry()
hon_scale.pack()

#scale 小時
# label_remind = ttk.Label(text="請输入幾小時前提醒(1~72):")#,showvalue=YES
# label_remind.pack(pady=20)
# hon_scale = ttk.Scale(root,from_= 1,to = 72,orient=HORIZONTAL)
# hon_scale.pack()
label = Label(root)  
label.pack() 
Label_y = ttk.Label(text= '2021/7',font=30)
Label_y.pack()
# print(hon_scale.get())
# remind_box = Entry()
# remind_box.pack()

treeview.bind('<Double-1>', set_cell_value)
root.bind("<Escape>", lambda x: root.destroy())
print()
root.mainloop()
