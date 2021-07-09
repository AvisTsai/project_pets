from tkinter import ttk
from tkinter import *
root = Tk()  # 初始框的聲明
columns = ("姓名", "IP地址")
treeview = ttk.Treeview(root, height=18, show="headings", columns=columns)  # 表格

treeview.column("姓名", width=100, anchor='center') # 表示列,不顯示
treeview.column("IP地址", width=300, anchor='center')

treeview.heading("姓名", text="姓名") # 顯示錶頭
treeview.heading("IP地址", text="IP地址")

hon_scale = ttk.Scale(root,from_= 1,to = 72,orient=HORIZONTAL)
hon_scale.pack()

treeview.pack(side=LEFT, fill=BOTH)

name = ['電腦1','服務器','筆記本']
ipcode = ['10.13.71.223','10.25.61.186','10.25.11.163']
for i in range(min(len(name),len(ipcode))): # 寫入數據
    treeview.insert('', i, values=(name[i], ipcode[i]))


def treeview_sort_column(tv, col, reverse):  # Treeview、列名、排列方式
    l = [(tv.set(k, col), k) for k in tv.get_children('')]
    l.sort(reverse=reverse)  # 排序方式
    # rearrange items in sorted positions
    for index, (val, k) in enumerate(l):  # 根據排序後索引移動
        tv.move(k, '', index)
    tv.heading(col, command=lambda: treeview_sort_column(tv, col, not reverse))  # 重寫標題，使之成爲再點倒序的標題

def set_cell_value(event): # 雙擊進入編輯狀態
    for item in treeview.selection():
        #item = I001
        item_text = treeview.item(item, "values")
        #print(item_text[0:2])  # 輸出所選行的值
    column= treeview.identify_column(event.x)# 列
    row = treeview.identify_row(event.y)  # 行
    cn = int(str(column).replace('#',''))
    rn = int(str(row).replace('I',''))
    entryedit = Text(root,width=10+(cn-1)*16,height = 1)
    entryedit.place(x=16+(cn-1)*130, y=6+rn*20)
    def saveedit():
        treeview.set(item, column=column, value=entryedit.get(0.0, "end"))
        entryedit.destroy()
        okb.destroy()
    okb = ttk.Button(root, text='OK', width=4, command=saveedit)
    okb.place(x=90+(cn-1)*242,y=2+rn*20)

def newrow():
    name.append('待命名')
    ipcode.append('IP')
    treeview.insert('', len(name)-1, values=(name[len(name)-1], ipcode[len(name)-1]))
    treeview.update()
    newb.place(x=120, y=(len(name)-1)*20+45)
    newb.update()

treeview.bind('<Double-1>', set_cell_value) # 雙擊左鍵進入編輯
newb = ttk.Button(root, text='新建聯繫人', width=20, command=newrow)
newb.place(x=120,y=(len(name)-1)*20+45)


for col in columns:  # 綁定函數，使表頭可排序
    treeview.heading(col, text=col, command=lambda _col=col: treeview_sort_column(treeview, _col, False))


root.mainloop() 