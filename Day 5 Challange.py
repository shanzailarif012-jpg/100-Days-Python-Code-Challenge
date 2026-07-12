                            # 100 Days Python Challange 
                        # Day Five(5) Python 25 Questions 
print("\t\t\t\t\tDev.Shanzail Backend Developer") # Name And Role

#1 ake your name and age as input and print: Hello Muhammad, you are 21 years old.

name = input("Enter Name: ")
age = int(input("Enter Age: "))
print(f"Hello {name} , you are {age} years old")

#2 ake two numbers and print:
'''Addition
Subtraction
Multiplication
Division
Modulus'''
# Problem 2 
num1 = int(input("enter num1: "))
num2 = int(input("enter num2: "))

print("Addition is",num1+num2) # Addition
print("Substraction is",num1-num2) # Substraction
print("Multiplication is",num1*num2) # Multiplication
print("Division is",num1/num2)# Division
print("Modulus is",num1%num2)# Modulus

#3 Take a string and print:
'''Length
First character
Last character
Reverse'''
# Problem 3 
greet = input("Enter Details: ")

print(len(greet))
print(greet[0])
print(greet[-1])
print(greet[::-1])

#4 Take a sentence and count how many spaces it contains.

user = input("Enter Name and City: ")
print(user.count(" "))

#5 Take a word and check whether it starts with a vowel.

vowels = ("a", "e", "i", "o", "u", "A", "E", "I", "O", "U")

word = input("Enter Word: ")

print(word.startswith(vowels))

#6 Create a list of 10 numbers and print only the even numbers. 

l1 = [10,15,14,16,8,19]

for num in l1:
    if num % 2==0:
        print(num)

#7 Create a list of 10 numbers and print only the odd numbers.
l2 = [ 2,3,6,3,1,7,8,9,4,24]

for num in l2:
    if num % 2!=0:
        print("Odd numbers are",num)

#8 Take 5 favorite programming languages in a list and print them using a loop.

l = ["Python","Pandas","JS","Html","CSS"]
i = 0
while i<len(l):
    print(l[i])
    i = i+1

#9 Create a tuple of 7 days and print Saturday and Sunday.
t = ("Mon","Tues","Wed","Thurs","Friday","Sat","Sun")
print(t[5])
print(t[-1])

#10 Create a dictionary containing:
'''Name
Age
City
Country
Profession
Print each key and value using a loop.'''
# Problem 10
profile = {
    "Name":"Shanzail",
    "Age":"21",
    "City":"Hyderabad",
    "Country":"Pakisatn",
    "Profession":"Software Developer"
}

for key , value in profile.items():
    print(key, ":" ,value)

#11 Take marks and print:
'''Pass
Fail
(Passing marks = 40)'''

marks = int(input("enter marks: "))

if marks<40:
    print("Fail")
else:
    print("Pass")

#12 Take a number and check whether it is:
'''
Positive
Negative
Zero'''
#Problem 12

num = int(input("Enter Num: "))

if num >0:
    print("Positive")
elif num<0:
    print("Negative ")
else:
    print("Zero")

#13 Take three numbers and print the smallest number.
n1 = int(input("Enter num1: "))
n2 = int(input("Enter num2: "))
n3 = int(input("Enter num3: "))

print(min(n1,n2,n3))

#14 Take a year and check whether it is:Leap Year Not Leap Year
year = int(input("enter year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year,"Is leap year")
else:
    print("This is not leap year",year)

#15 Take a character and check:
'''Uppercase
Lowercase
Digit
Special Character'''
#Problem 
charcter = input("enter word: ")

if charcter.isupper():
    print("Uppercase")
elif charcter.islower():
    print("Lowwercase")
elif charcter.isdigit():
    print("Digit")
else:
    print("Special Character")

#16 Print numbers from 1 to 50 divisible by 7.

for i in range(1,51):
    if i % 7 == 0:
        print(i)

#17 Print numbers from 100 to 1.

for i in range(100,0,-1):
    print(i)

#18 Print the multiplication table of any number entered by the user.

user = int(input("enter num: "))

for i in range(1,11):
    print(f"{user} * {i} = {user*i}")

#19 Find the factorial of a number.

num = int(input("enter factorial num: "))
factorial = 1
for i in range(1,num+1):
    factorial = factorial*i
print(factorial)

#20 Print the sum of all even numbers between 1 and 100.

total = 0
for i in range(1,101):
    if i % 2==0:
        total = total + i
print(total)

#21 Print numbers from 1 to 30 but skip:

for i in range(1,31):
    if i % 5==0:
        continue
    print(i)

#22 Keep asking the user to enter a number until they enter 50

correct = 50
user = int(input("Enter Num: "))
i = 0
while correct != user:
    print("Again")
    user = int(input("Enter No: "))
    i = i+1
else:
    print("Correct")

#23 Print numbers from 1 to 100, but stop immediately when you reach 55.

for i in range(1,101):
    if i ==55:
     print("Found 55")
     break
    print(i)

#24 Print this pattern:
'''1
12
123
1234
12345'''
# Problem 24 

n = int(input("Enter Num: "))

for i in range(1, n+1):
    for j in range(1, i+1):
        print(j, end="")
    print()

#25 Take a number n from the user and print:
'''*
**
***
****
*****
****
***
**
*
'''
# Problem 25

n = int(input("Enter Num: "))

for i in range(1,n+1):
    print("*" *i)
for i in range(n-1,0,-1):
    print("*"*i)

# TimeTaken = 83Mint
# 🏆 100 Days Python Challenge – Day 5 Result
# Score: ⭐⭐⭐⭐⭐⭐⭐⭐⭐☆ (9.8/10)
# Overall Rating: 98/100 🏆 Python Master