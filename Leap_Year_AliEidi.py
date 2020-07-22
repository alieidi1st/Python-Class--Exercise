# Leap year Code
# by ALi Eidi
year = int (input(' Please enter the year:  '))
if (((year % 4 == 0) and (year % 100!= 0)) or ((year % 100==0) and (year % 400==0))):
    print ('This is a leap year')
else:
    print (' This is not a leap year')
                   
