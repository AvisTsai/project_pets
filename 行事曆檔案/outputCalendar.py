from datetime import *
import calendar

todayy  = date.today()
default_y = todayy.year
default_m = todayy.month

'''class CustomHTMLCal(calendar.HTMLCalendar):
    cssclasses = [style + " text-nowrap" for style in
                  calendar.HTMLCalendar.cssclasses]
    cssclass_month_head = "text-center month-head"
    cssclass_month = "text-center month"
    cssclass_year = "text-italic lead"'''

'''
#TextCalendar
c =calendar.TextCalendar(calendar.SUNDAY) 
str = c.formatmonth(default_y,default_m)'''
print(str)

#HTMLCalendar
hc =calendar.HTMLCalendar(calendar.SUNDAY) 
str = hc.formatmonth(default_y,default_m)
data=open("output2.txt",'w+') 
print(str,file=data)
data.close()

'''
c =calendar.TextCalendar(calendar.SUNDAY)
for i in c.itermonthdays(default_y,default_m):
    print(i)

for name in calendar.month_name:
        print(name)

for day in calendar.day_name:
        print(day)
listWeek = ['Sun','Mon','Tue','Wed','Thu','Fri','Sat']
print(listWeek)

a = calendar.calendar(2021, w=3, l=1, c=6, m=3)
print(a)'''