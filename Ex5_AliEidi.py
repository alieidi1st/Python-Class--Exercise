#069
"""t1 = ('iran' , 'turkey' , 'netherlands' , 'denmark' , 'italy')
print (t1)
l1 = list(t1)
s1 = input ('Please select one of the countries from the list: ')
s1 = s1.lower()
a1 = l1.index(s1)
print ('You selected country number: ',a1+1)
"""
#070
"""t1 = ('iran' , 'turkey' , 'netherlands' , 'denmark' , 'italy')
print (t1)
l1 = list(t1)
s1 = int (input ('Please select one of the countries from the list wiht a number: '))
a1 = l1[s1-1]
print ('You selected country is: ',a1)
"""
#071
"""l1 = ['soccer' , 'wrestling']
s1 = input('Please enter your favourite sport: ')
if s1 not in l1:
    l1.append(s1)
    l1.sort()
print (l1)
"""
#072
"""l1 = ['math' , 'physics', 'chemistry' , 'biology' , 'geography']
print (l1)
s1 = input ('Which of these subjects you don not like? ')
a1= l1.index(s1)
l1.remove(l1[a1])
print (l1)
"""
#073
"""print ('Please enter 4  of your favourite foods')
d1 = {}
d2 = {}
for food in range (1,5):
    print ('My Favourite fodd number ', food, 'is: ')
    v1 = input()
    d1.update({v1:food})
print (d1)
v2 = input('Which food do you eant to remove from the list? ')
d1.pop(v2, None)
print (d1)
"""
#074
"""l1 =['blue', 'green' , 'red', 'yellow' , 'white' , 'black', 'purple', 'brown' , 'pink', 'orange']
print (l1)
a1 = int(input('Please insert a starting number between 0 and 4: '))
a2 = int(input('Please insert a ending number between 5 and 9: '))
if not (a1>= 0 and a1 <=4 and a2>=5 and a2<=9):
    print('Error message')
print (l1[a1:a2])
"""
#075
"""l1 = [123 , 345 , 456 , 789]
for number in l1:
    print (number)
a1 = int (input ('Please enter a three digit number: '))
if a1 in l1:
    print (l1.index(a1))
else:
    print ('That is not in the list')
"""
#076
"""print ('Please enter the name of three people ypu want to invite to a party')
l1 =[]
g1 = input ('My first guest name is: ')
l1.append(g1)
g1 = input ('My second guest name is: ')
l1.append(g1)
g1 = input ('My third guest name is: ')
l1.append(g1)
a1 = 'yes'
while a1 == 'yes':
    a1 = input ('Do you want to add another guest? ')
    a1.lower()
    if a1 == 'yes':
        g4 = input ('Whose your next guest? ')
        if g4 not in l1:
            l1.append(g4)
    elif a1 == 'no':
        print ('Number of your guest is: ', len(l1)+1)
    else:
        print ('Wrong answer')
"""
#077
"""print ('Please enter the name of three people ypu want to invite to a party')
l1 =[]
g1 = input ('My first guest name is: ')
l1.append(g1)
g1 = input ('My second guest name is: ')
l1.append(g1)
g1 = input ('My third guest name is: ')
l1.append(g1)
a1 = 'yes'
while a1 == 'yes':
    a1 = input ('Do you want to add another guest? ')
    a1.lower()
    if a1 == 'yes':
        g4 = input ('Whose your next guest? ')
        if g4 not in l1:
            l1.append(g4)
    elif a1 == 'no':
        print ('Your guests list is: ', l1)
        g4 = input ('Please choose one of the guests from the list: ')
        print ('You chose guest number: ', l1.index(g4)+1)
        a1 = input('Do you still want this chosen guest to come to the party? ')
        a1.lower()
        if a1 == 'no':
            l1.remove(g4)
            print ('your guest list is: ',l1)
    else:
        print ('Wrong answer')
"""
#078
"""print ('Here is a list of some TV shows')
l1 = ['Movie time', '14 news', 'football live', 'documentary']
for program in l1:
    print (program)
a1 = input('Please enter another show name: ')
if a1 not in l1:
    p1 = int (input('Which position do you want to insert it in the list? '))
    l1 = l1[0:(p1-1)] + [a1] + l1[(p1-1):4]
    print (l1)
"""
#079
"""nums = []
for i in range (0,3):
    n1 = int (input('please enter a number: '))
    nums = nums + [n1]
a1 = input('Do you still want to save the last number you entered? ')
a1.lower()
if a1 == 'no':
    nums.remove(n1)
print (nums)
"""
    
