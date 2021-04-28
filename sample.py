import datetime

curr_date = datetime.datetime.now()  #Get curr datetime
print(curr_date)

print(curr_date.year)  #Get the year, month and day  of type int
print(curr_date.month)
print(curr_date.day)

print(type(curr_date.day))


print(curr_date.strftime("%d")) #Day of month 1-31
print(curr_date.strftime("%w"))  # weekday as num - 0 is Sunday 
print(curr_date.strftime("%a")) #Weekday short
print(curr_date.strftime("%A"))  #Get the weekday

print(curr_date.strftime("%m")) #Month as num  1-12
print(curr_date.strftime("%b"))  #Month short
print(curr_date.strftime("%B"))  #Get the month name
print(curr_date.strftime("%y"))  #year short
print(curr_date.strftime("%Y"))   #Year 

print(curr_date.strftime("%H"))  #Hour 0-23
print(curr_date.strftime("%I"))  #Hour 0-12
print(curr_date.strftime("%M"))  #Minute
print(curr_date.strftime("%S"))  #Second
print(curr_date.strftime("%p"))  #AM/PM
print(curr_date.strftime("%Z"))  #Timezone

#Create a datetiem object
new_date = datetime.datetime(2021,8,2,12,0,0)
print(new_date)

