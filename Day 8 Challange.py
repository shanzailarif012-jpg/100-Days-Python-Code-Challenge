                            #  100 Days Python Challange 
                        # Day Eight(8) Python 25 Questions 
print("\t\t\t\t\tDev.Shanzail Backend Developer") # Name And Role

#1 Create a function add(a, b) that returns the sum of two numbers. Print the returned value.

def add(a,b):
    return(a+b)

sum = add(8,8)
print(sum)

#2 Create a function subtract(a, b) that returns the difference of two numbers.
def sub(a,b):
    return(a-b)

result=sub(5,3)
print(result)

#3 Create a function multiply(a, b) that returns the product of two numbers.
def multiply(a,b):
    return(a*b)

result=(5*5)
print(result)
#4 Create a function divide(a, b) that returns the division of two numbers.
def division(a,b):
    return(a//b)

divide=division(10,2)
print(divide)

#5Create a function square(num) that returns the square of a number.
def square(a):
    return(a**2)
answer= square(6)
print(answer)

#6 Create a function that returns "Even" if the number is even, otherwise returns "Odd".

def check_even_odd(num):
    if num % 2==0:
        return("Even")
    else:
        return("Odd")
    
result=(check_even_odd(13))
print(result)

#7 Create a function that returns "Positive", "Negative", or "Zero"
def check_type(num):
    if num>0:
        return("Postive Num",num)
    elif num<0:
        return("Negative Num",num)
    else:
        return("Zero",num)
    
result=check_type(12)
print(result)

#8 Create a function that returns the greater of two numbers.
def greater_num(a,b):
    if a>b:
        return("Greater num is A",a)
    else:
        return("Greater num is B",b)

answer = greater_num(1,7)
print(answer)

#9 Create a function that returns the largest of three numbers.

def largest(a,b,c):
    if a>b and a>c:
        return("Num A is Largest",a)
    elif b>a and b>c:
        return("Num B is Largest",b)
    elif c>b and c>a:
        return("Num C is Largest",c)
    
answer=largest(21,16,8)
print(answer)

#10 Create a function that returns True if a year is a leap year, otherwise False.
def leap_year(num):
    if num %  400 == 0:
        return("Leap Year")
    elif num % 100 == 0:
        return("Not Leap Year")
    elif num % 4 ==0:
        return("Leap Year")
    else:
        return("Not Leap Year")
    
check = leap_year(2031)
print(check)

#11 Create a function/greet(name="Guest")
def greet(name="Guest"):
    print("Hey",name)

greet()

#12 Create a function: country(name="Pakistan")

def country(name="Pakistan"):
    print("My Country Name is: ",name)

country("America") # By Keyword Argument
country() # By Deafult Argument

#13 Create a function: power(number, exponent=2)/Return the result.
def power(num,exponent=2):
    return(num**exponent)

result = power(3)
print(result)

#14 Create a function: student(name, city="Hyderabad") /Print both values.
def student(name,city="Hyderabad"):
    print(name,city)
student("Shanzail")


#15 Create a function: discount(price, discount=10) /Return the final price after discount.
def discount(price,discount=10):
    return((price*discount)/100)
# price = int(input("Enter Price")) # For Enter User price 
total=discount(4500)
finalprice = 4500-total
print(finalprice)

#16 Call a function using keyword arguments.
'''Example:
student(name="Ali", age=20)
Roman Urdu:
Arguments order change karke keyword arguments use karo.'''
# Problem 16 

def student(name="Ali", age=20):
    print(name, age)

student(age=20, name="Ali")

#17 Create a function with three parameters and call it using keyword arguments.

def three(a,b,c):
    print(b,a,c)
three(a="Shanzail",b="Ali",c="Shahid")

#18 Create a function that prints employee information using keyword arguments.
'''Parameters:
name
department
salary'''
#Problem 18

def employee(name,department,salary):
    print(name,department,salary)

employee(name="Shanzail",department="CS",salary="45000")

#19 Create a local variable inside a function and print it./Then try printing it outside the function. /Observe what happens.

def variable(name):
    print(name)
    city="Hyderabad" # Local Variable

variable("Shanzail")
# print(city) local Variable outside from function

#20 Create a global variable named company. /Print it inside and outside the function.

company = "Shanzail Codes Solutions" # Use of Global Variable

def name():
    print(company) # call in function

name()
print(company) # call outside the function

#21 Create two functions. /Both should have a variable named x. /Print both values.

def check1(x):
    print(x)
def check2(x):
    print(x)

check1(15)
check2(5)

#22 Create a function that returns the factorial of a number.

def factorial(num):

    factorial=1
    for i in range(1,num+1):
      factorial=factorial*i
    return factorial
    
result=(factorial(5))
print(result)

#23 Create a function that returns whether a number is Prime or Not Prime. 

def prime_num(num):
    for i in range(2,num):
        if num % 2==0:
            return("Not Prime Num")
        else:
            return("Prime Num")
        
result =prime_num(98)
print(result)

#24 Create a function that returns the first 10 Fibonacci numbers as a list.
def fibonacci(num):
    a = 0
    b = 1
    number=[]
    for i in range(num):
        number.append(a)
        c = a + b 
        a = b 
        b = c
    return number
check=fibonacci(10)
print(check)


#25 Create a function:
'''student_result(name, roll_no, eng, maths, phy, chem, bio)
The function must return:
Total
Average
Grade
Result (PASS/FAIL)
Then, outside the function,print all in this format
========== STUDENT RESULT ==========
Name      :
Roll No   :
Total     :
Average   :
Grade     :
Result    :
===================================='''

name=input("Enter Name: ")
rollnum = int(input("Enter RollNum: "))
eng=int(input("Enter English Marks: "))
math=int(input("Enter Maths Marks: "))
phy=int(input("Enter Physics Marks: "))
chem=int(input("Enter Chemistry Marks: "))
bio=int(input("Enter Bio Marks: "))

def student_result(name,rollnum,eng,math,phy,chem,bio):
    total=(eng+math+phy+chem+bio)
    average= total//5
    
    if average>=90:
        grade="A+"
    elif average>=80:
        grade="A"
    elif average>=70:
        grade="B"
    elif average>=60:
        grade="C"
    else:
        grade="Fail"
    
    if average>=60:
     result="Pass"
    else:
        result="Fail"
    
    return name,rollnum,total,average,grade,result
    
name, rollnum, total, average, grade, result = student_result (name, rollnum, eng, math, phy, chem, bio
)

print("\n\t\t\t========== STUDENT RESULT ==========")
print("Name: ",name)
print("RollNum: ",rollnum)
print("Total: ",total)
print("Grade: ",grade)
print("Average: ",average)
print("Result: ",result)
print("=================================================")

# TimeTaken = 70Mint
# 🏆 100 Days Python Challenge – Day 8 Review
# Score: 97/100 🌟
# Rating: ⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐ (9.7/10)