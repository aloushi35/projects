# Fakhreddine, Ali
#Problem 1

pi=3.14
radius = float(input('Enter a radius: '))
height = float(input('Enter a height: '))
volume = pi * radius * radius * height
print("The volume is", volume)


#Problem 2

first = input("Enter a first name: ")
last = input("Enter a last name: ")
print (first + " " + first + " " + last + last + last)


#Problem 3

first = input("Enter the first sequence of numbers separated by commas: ")
second = input("Enter the second sequence of numbers separated by commas: ")
first = [int(x) for x in first.split(',')]
second = [int(x) for x in second.split(',')]
result = []
for j in first:
    for i in second:
        result.append((j,i))
print("Coordinates: ",result)


#Problem 4

x = abs(float(input('Enter a number: ')))
value = x**(1/3)
print('Result: ',value)


#Problem 5


import random

number = random.randint(1,100)
while True:
    print('Enter a number: ')
    guess = input()
    guess = int(guess)


    if guess < number:
        print('The number is greater than', guess)

    if guess > number:
        print('The number is less than', guess)

    if guess == number:
        print('Congratulations! The number is',guess)
        break


#Problem 7

#a
sum = 0
for i in range(10,20,1):
    if(i%2 == 1):
        sum=sum + i
print('The sum of the five odd integers from 10-20 is:',sum)

#b
num = 66**4
print('66 to the 4th power is:',num)

#c
mass = 40
velocity = 10
KE = 0.5 * mass * velocity
print('The kinetic energy is:',KE)


#Problem 8

test_scores = '2 5 6 9 3 8 2 6 5 9 5 6 6 2 9 0 9 8 8 7'
#1
print('The quiz score for the 2nd student is', test_scores[2])

#2
print('The quiz score for the 14th student is', test_scores[26])

#3
print('The quiz score for the 8th student plus 9th student is',int(test_scores[14])+int(test_scores[16]))

#4
print('The quiz score for the 19th student subtracted by the 3rd student is', int(test_scores[36])-int(test_scores[4]))


#Problem 9

s = 'computerscience'
char = s.endswith('b')
#a
print("The last character of string s is 'b':", char)

#b
char2 = s.startswith('c')
print("The first character of string s is 'c':", char2)

#c
char3 = s.count('e') == 3
print("There are three 'e' in string s:", char3)

#d
char4 = len(s) == 16
print("The length of string s is 16:", char4)


#Problem 10

a = type(1.1*2)==int
print('The type of a float multiplied by an int is an int:',a)

#b
b = len(['a','b','c','d','e']*3)==15
print('Multiplying list by 3 will result in a length of 15:',b)

#c
c = 20%5 <=2
print('The remainder when 20 is divided by 5 is less than or equal to 2:',c)

#d
d = (5%4!=0 and 5%3!=0 and 5%2!=0 and 4%2!=0)
print('Five is a prime number and four is an odd number:',d)

#e
e = type(62)==float
print('The number 62 is type float:',e)


#Problem 11

s = 'abcdefghijklmnopqrstuvwxyz'

#a
print(s[7]+s[0]+s[17]+s[17]+s[8]+s[18])

#b
print(s[11]+s[0]+s[1])

#c
print(s[13]+s[4]+s[22])

#d
print(s[12]+s[12]+s[12]+s[24]+s[22])
