day = int(input ('input day of month: '))
month = int(input ('input month of year: '))
year = int (input ('input year in two-digit form:'))


print (f'{day} / {month} / {year}' )
if day * month == year:
    print ('this date is magic')
else:
    print ('this date is not magic')

