#045
"""total = 0
while total <= 50:
    num = int (input('Plase enter a number: '))
    total += num
    print ('The  total is: ', total)
"""
#046
"""num = 0
while num < 5:
    num = int(input('Please enter a number: '))
print ('The last number you entered was: ', num)
"""
#047
"""n1 = int (input('Please enter a number: '))
sum1 = int(input('Please enter another number: '))
sum1 += n1
a1 = 'y'
while a1 == 'y':
    a1 = input ('Do you want to adsd another number? [y/n]')
    if a1 == 'y':
        n1 = int(input('What is the next nunmber? '))
        sum1 += n1
print ('The total amount is: ', sum1)
"""
#048
"""count =0
l1 = []
p1 = input('Who do you want to invite to the party? ')
l1 += [p1]
print (p1 , 'has now been invited.')
count += 1
ans = 'y'
while ans == 'y':
    ans = input('Do you want to invite somebody else? [y/n] ')
    if ans == 'y':
        p2 = input ('Who is next guest? ')
        count += 1
        l1 += [p2]
    else:
        print ('The number of guests is: ', count)
"""
#049
"""compnum = 50
guess = 0
count =0
while guess != compnum:
    guess = int(input ('Guess the ecompnum: '))
    count += 1
    if guess > compnum:
        print ('Too high')
    elif guess < compnum:
        print ('Too low')
print ('Well done, you took ', count,"attempts.")
"""
#050
"""num =0
while num <10 or num >20:
    num = int (input('Please enter a number between 10 and 20: '))
    if num <10:
        print ('Too low')
    elif num >20:
        print ('Too high')
print('Thank you')
"""
#051
"""num = 10
while num >0:
    print ('There are ', num, 'green bottles hanging on the wall, ', num, 
          'green bottles hanging on the wall, and if 1 green bottle should accidently fall')
    n1 = int(input('How many green bottles will be hanging on the wall? '))
    while n1 != (num-1):
        print ('No try again')
        n1 = int(input('How many green bottles will be hanging on the wall? '))
    print ('There will be ', n1,'green bottles hanging on the wall')
    num -= 1
"""
