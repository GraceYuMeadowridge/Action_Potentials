import calendar
#create a plain text calendar

c = calendar.TextCalendar(calendar.SUNDAY)
str = c.formatmonth(2021,5)
print(str)

d = calendar.TextCalendar(calendar.SUNDAY)
strd = d.formatmonth(2021,7)
print(strd)