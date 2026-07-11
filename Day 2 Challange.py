                        # 100 Days Python Challange 
                        # Day Two(2) Python 25 Questions 
print("\t\t\t\t\tDev.Shanzail Backend Developer") # Name And Role

#1 Create two variables a = 25 and b = 10. Print their addition.
a=25
b=10
print(a+b)

#2 Print subtraction, multiplication, division, floor division, modulus, and exponent using a and b.

print("Subtraction is",a-b)
print("Multiplication is",a*b)
print("Division is",a/b)
print("Floor Division is",a//b)
print("Modulus is",a%b)
print("Exponent is",a**b)

#3 Check whether a is greater than b.
print(a>b)

#4 Check whether a is equal to b
print(a==b)

#5 Create two boolean variables and use and, or, and not.

print("Truth Table of 'AND'")
print(True and False)
print(False and True)
print(True and True)
print(False and False)
print("\nTruth Table of 'OR'")
print(True or False)
print(False or True)
print(True or True)
print(False or False)

print("\nTruth Table of 'NOT'")
print(not(True))

#6 Take the user's name as input and print:Hello, <name>!

user = input("Enter Your Name: ")
print("Hello",user)

#7 Take the user's age and print it.

age=int(input("Enter Your Age: "))
print("Age is",age)

#8 Take two numbers from the user and print their sum.

no1= int(input("Enter First Num: "))
no2= int(input("Enter Second Num: "))
print("Sum of 2 num is:",no1+no2)

#9 Take a city name from the user and print it in uppercase.

cityname = input("Enter City Name: ")
print(cityname.upper())

#10 Take a word from the user and print its length.

word=input("Enter Your Country: ")
print(len(word))

#11 Take a number as input and convert it into an integer.

num0= input("Enter Num: ")
print(type(num0))
convertnum=(int(num0))
checktype = print(type(convertnum))

#12 Convert an integer 50 into a float

num50=50
print(type(num50))

convertnum50=(float(num50))
print(convertnum50,type(convertnum50))

#13 Convert a float 99.99 into an integer.

numfloat = 34.877
convertnumfloat=(int(numfloat))
print(convertnumfloat,type(convertnumfloat))

#14 Convert the integer 100 into a string.

num100 = 100
print(num100,type(num100))
convert=str(num100)
print(convert,type(convert))

#15 Print the data type after each conversion

num = input("Enter Num: ")
print(num,type(num))

num1=(int(num))
print(num1,type(num1))

num2=(float(num1))
print(num2,type(num2))

num3=bool(num2)
print(num3,type(num3))

#16 Calculate the area of a rectangle using user input.


length = int(input("Enter length: "))
width = int(input("Enter width Area: "))

area = length*width
print("Area is", area)

#17 Calculate the perimeter of a rectangle.
length = int(input("Enter length:"))
width = int(input("Enter width:"))

perimter = 2*(length+width)
print(perimter)

#18 Take the radius of a circle and calculate its area.(Use 3.14 for π.)

radius = int(input("Enter Radius of circle: "))

area = 3.14 * radius*radius
print(area)

#19 Take marks of 5 subjects and calculate the total.

mark1= int(input("Enter Marks1: "))
mark2= int(input("Enter Marks2: "))
mark3= int(input("Enter Marks3: "))
mark4= int(input("Enter Marks4: "))
mark5= int(input("Enter Marks5: "))

totalmarks = sum([mark1,mark2,mark3,mark4,mark5])
print("total marks is: ",totalmarks)

#20 Calculate the average of those 5 subjects.

average= totalmarks/5
print(average)

#21 Take your full name as input and print it in lowercase.

name = input("Enter Your Name: ")
print(name.lower())

#22 Print the first and last character of the entered name. 

print(name[0])
print(name[-1])

#23 count how many times the letter "a" appears in the entered name.

print(name.count("a"))

#24 Replace all spaces in the entered sentence with underscores (_).

greet = ("Hey iam Shanzail HELLO Everyone")

replace=greet.replace(" ","_")
print(replace)

#25 ⭐ Challenge
'''Take the user's:
Name
Age
City
Favorite Programming Language
Then print a formatted profile like:

========== PROFILE ==========
Name : Muhammad Shanzail
Age  : 21
City : Hyderabad
Language : Python
============================='''

name = input("Enter Name: ")
age = int(input("Enter Age: "))
city=input("Enter City: ")
programming = input("Enter Fav Programming Language: ")
print("\t\t Profile")
print("Name",name)
print("age",age)
print("city",city)
print("Fav programming",programming)

# Total Mint Taken = 56.70sec
# 🏆 100 Days Python Challenge – Day 2 Result
# Score: ⭐⭐⭐⭐⭐⭐⭐⭐⭐☆ (9.6/10)
# Overall Rating: 96/100 🥇 Gold
# 🔥 Great improvement from Day 1. Keep this consistency
# you're building a very strong Python foundation