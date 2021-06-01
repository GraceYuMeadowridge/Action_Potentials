import calendar
#create a plain text calendar

c = calendar.TextCalendar(calendar.SUNDAY)
str = c.formatmonth(2021,5)
print(str)