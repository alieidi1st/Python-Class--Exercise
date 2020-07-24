day = int (input ('Please enter the day: '))
month = int (input('Please enter the month as an integer: '))
year = int (input('Please enter the year: '))
Month_days = [31,28,31,30,31,30,31,31,30,31,30,31]
if  day <1 or month >12 or month <1:
    print ('You entered wrong date')
else:
    if day > Month_days[month]:
     print ('You entered wrong date')
    if (((year % 4 == 0) and (year % 100!= 0)) or ((year % 100==0) and (year % 400==0))):
        Month_days [2] = 29
        day_number = sum (Month_days[: month-1])+ day        
        print ('This is a leap year and day number: ', day_number)
    else:
        day_number = sum (Month_days[: month-1])+ day
        print ('This is not a leap year and day number: ', day_number)
                   
