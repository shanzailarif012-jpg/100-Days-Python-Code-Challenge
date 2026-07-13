                            # 100 Days Python Challange 
                        # Day Seven(7) Python 25 Questions 
print("\t\t\t\t\tDev.Shanzail Backend Developer") # Name And Role

#1 Create a function named greet() that prints:

def greet():
    print("Welcome to Python Programming")
greet()

#2 Create a function my_name() that prints your full name.

def my_name():
    print("Muhammad Shanzail")
my_name()

#3 Create a function developer() that prints:

def developer():
    print("I want to become a Backend Developer.")

developer()

#4 Create a function table_of_five() that prints the multiplication table of 5.

def table_of_five(n):
    for i in range(1,11):
        print(f"{n} * {i} = {5*i}")

table_of_five(5)

#5 Create a function line() that prints:
'''==============================
Call it 3 times.'''
#Problem 5

def line():
    print("==============================")
line()
line()
line()

#6 Create a function greet(name) that prints:
'''Hello Muhammad
Use user input while calling the function.'''
# Problem 6
def greet():
    user = input("Enter Name: ")
    print("Hello",user)

greet()

#7 Create a function square(num) that prints the square of a number.

def num(n):
    print(n*n)
num(7) # 1st call
num(6) # 2nd call

#8 Create a function cube(num) that prints the cube of a number.

def cube(n):
    print(n*n*n)

cube(7)

#9 Create a function addition(a, b) that prints the sum of two numbers.

def add():
    a = int(input("Enter num1: "))
    b = int(input("Enter num2: "))
    total = a+b
    print(f"Sum of a and b is: {total}")
add()

#10 Create a function student(name, age) that prints:
'''Name : Muhammad
Age  : 21'''
#Problem 10
def student():
    name = input("Enter Name: ")
    age = int(input("Enter Age: "))

    print("Name :", name)
    print("Age  :", age)

student()

#11 Create a function that takes 3 numbers and prints the largest number.

def largest():
    num1 = int(input("Enter num1: "))
    num2 = int(input("Enter num2: "))
    num3 = int(input("Enter num3: "))

    print(max(num1,num2,num3))

largest()

#12 Create a function that takes length and width and prints the area of a rectangle.

def rectangle():
    len = int(input("Enter Length: "))
    width = int(input("Enter width: "))

    print(f"Area of rectangle is: {len*width}")

rectangle()

#13 Create a function that takes radius and prints the area of a circle.(Use 3.14)

def radius():
    radius= int(input("Enter Aera: "))

    print(f"Area of Circle is: {3.14 * radius * radius}")

radius()

#14 Create a function that takes 5 subject marks and prints:Total/Average
def marks():
    a = int(input("Enter English Marks: "))
    b = int(input("Enter Maths Marks: "))
    c = int(input("Enter Islamiyat Marks: "))
    d = int(input("Enter chemistry Marks: "))
    e= int(input("Enter Physics Marks: "))

    total = (a+b+c+d+e)
    average = (total/5)
    print(f"Total is: {total}")
    print(f"Average is: {average}")

marks()

#15 Create a function that takes name and city and prints:Muhammad lives in Hyderabad.

def details():
    name = input("Enter Name: ")
    city = input("Enter City: ")
    print(f"{name} lives in {city}")

details()

#16 Create a function that prints numbers from 1 to 10.

def num():
    for i in range(1,11):
        print(i)
num()

#17 Create a function that prints all even numbers from 1 to 50.
def even_num():
    for i in range(1,51):
        if i % 2==0:
            print(i)

even_num()

#18 Create a function that prints the multiplication table of any number.Take the number from the user.

def multiply():
    n = int(input("Enter Table num: "))
    for i in range(1,11):
        print(f"{n} * {i} = {n*i}")

multiply()

#19 Create a function that prints the first 10 Fibonacci numbers.
def fib_num():
    a = 0
    b = 1
    for i in range(1,11):
        next = a + b
        a = b
        b = next
        print(next)
        print(a)
         
fib_num() # Note Formula Tora aur chatgpt se poucha hay

#20 Create a function that prints all factors of a number.
def factor():
   num = int(input("Enter Number: "))

   for i in range(1, num + 1):
    if num % i == 0:
        print(i)

factor()

#21 Create a function that checks whether a number is Even or Odd.

def check():
    num = int(input("Enter Num: "))
    if num % 2 == 0:
        print("Even Num")
    elif num ==0:
        print("Zero")
    else:
        print("Odd Number")

check()

#22 Create a function that checks whether a number is Positive, Negative, or Zero.

def checknum():
    num = int(input("Enter Num: "))
    if num >0:
        print("Positive Number")
    elif num<0:
        print("Negative Number")
    else:
        print("Zero")
checknum()

#23 Create a function that checks whether a year is a Leap Year.

def check_year():
    year = int(input("Enter year: "))
    if year % 400 == 0:
        print(year,"Leap Year")
    elif year % 100 == 0:
     print(year,"Not leap year")
    elif year % 4 == 0:
     print(year,"Leap Year")
    else:
        print(year,"Not Leap year")
check_year()

#24 Create a function that checks whether a number is Prime.

def check_num():
    num = int(input("Enter Number: "))

    if num <= 1:
        print("Not Prime")
        return

    for i in range(2, num):
        if num % i == 0:
            print("Not Prime")
            return

    print("Prime")

check_num()

#25 Create a function:report_card(name, roll_no, english, maths, physics, chemistry, biology)
'''
The function should print:
========== REPORT CARD ==========
Name      :
Roll No   :
Total     :
Average   :
Grade     :
Result    :
=================================
Use the same grading rules you've already practiced:
90–100 → A+
80–89 → A
70–79 → B
60–69 → C
Below 60 → Fail
'''
#Problem 25
def report_card():
    name = input("Enter Name: ")
    rollnum=int(input("Enter RollNum: "))
    subject1 = int(input("Enter English Marks: "))
    subject2 = int(input("Enter Maths Marks: "))
    subject3 = int(input("Enter physics Marks: "))
    subject4 = int(input("Enter Chemistry Marks: "))
    subject5 = int(input("Enter Biology Marks: "))

    total = (subject1+subject2+subject3+subject4+subject5)
    average=(total/5)

    if average >=90:
     Grade =("A+")
    elif average>=80:
       Grade = ("A")
    elif average>=70:
       Grade = ("B")
    elif average>=60:
       Grade = ("C")
    if average>=60:
       result=("Pass")
    else:
       result=("Fail")
    
    
    # Print All 
    print("---------------ReportCard---------------")
    print(f"Name: {name}")
    print(f"Rollnum: {rollnum}")
    print(f"Total: {total}")
    print(f"Average: {average}")
    print(f"Grade: {Grade}")
    print(f"Result: {result}")
    print("=================================")
    
report_card()

# TimeTaken = 72Mint
# 🏆 100 Days Python Challenge – Day 7 Result
# Score: ⭐⭐⭐⭐⭐⭐⭐⭐⭐☆ (9.6/10)
# Overall Rating: 96/100 🥇 Gold