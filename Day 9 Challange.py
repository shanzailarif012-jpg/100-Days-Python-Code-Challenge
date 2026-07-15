                        #  100 Days Python Challange 
                        # Day Nine(9) Python 25 Questions 
print("\t\t\t\t\tDev.Shanzail Backend Developer") # Name And Role

#1 Create a function maximum(a, b) that returns the larger number.

def max(a,b):
    if a>b:
        return("A is Greater")
    else:
        return("B is Greater")

checkmax=max(3,5)
print(checkmax)

#2 Create a function minimum(a, b) that returns the smaller number.

def min(a,b):
    if a<b:
        return("A is Smaller")
    else:
        return("B is Smaller")
    
checkmin=min(5,1)
print(checkmin)

#3 Create a function average(a, b, c) that returns the average of three numbers.
def avg(a,b,c):
    total = (a+b+c)/3
    return(total)
checkavg=avg(1,2,5)
print(checkavg)

#4 Create a function area_rectangle(length, width) that returns the area of a rectangle.
def area_rectangle(l,w):
    return(l*w)
checkarea=area_rectangle(5,7)
print(checkarea)

#5 Create a function simple_interest(principal, rate, time) that returns the simple interest.

def simple_interest(pricipal,rate,time):
    return(pricipal * rate * time) /100

checksimple_interest=simple_interest(3,5,7)
print(checksimple_interest)

#6 Create a function that returns "Pass" if marks are 40 or above, otherwise "Fail".

def marks(n):
    if n>40:
        return("PASS")
    else:
        return("FAIL")
n = int(input("Enter marks here: "))
checkresult= marks(n)
print(checkresult)

#7 Create a function that returns the grade:
'''90–100 → A+
80–89 → A
70–79 → B
60–69 → C
Below 60 → Fail'''
#Problem 7

def garde(n):
    if n>=90:
        return("A+")
    elif n>=80:
        return("A")
    elif n>=70:
        return("B")
    elif n>=60:
        return("C")
    else:
        return("FAIL")
n = float(input("Enter Marks Percentage To Check Grade: "))  # Use Flaot for Decimal In garde enter by user
checkgarde=garde(n)
print(checkgarde)

#8 Create a function that returns whether a character is:
'''Alphabet
Digit
Special Character'''
#Problem 8 
def whether(n):
    if n.isalpha():
     return("Alphabet")
    elif  n.isdigit():
       return("Digit")
    else:
       return("Special Character")
n = input("Enter Character: ")
checkwheather = whether(n)
print(checkwheather)

#9 Create a function that returns "Adult" if age is 18 or above, otherwise "Minor".
def age(n):
    if n>18:
        return("Adult")
    else:
        return("Minor")
n = int(input("Enter Your Age: "))
checkage=age(n)
print(checkage)

#10 Create a function that returns whether a number is divisible by both 3 and 5.
def divisible(n):
    if n % 3 == 0 and n % 5 == 0:
        return("Yes")
    else:
        return("No")
n = int(input("Enter Num: "))
checkdivisible=divisible(n)
print(checkdivisible)

#11 Create a function that returns the sum of numbers from 1 to n.
def sum_num(n):
    add = 0
    for i in range(1,n+1):
        add +=i
    return add
checksum=sum_num(10)
print(checksum)

#12 Create a function that returns the sum of all even numbers from 1 to n.

def sum_even(n):
    add = 0
    for i in range(1,n+1):
        if i %2==0:
            add += i
    return add

checksum_even=(sum_even(10)) 
print(checksum_even)

#13 Create a function that returns the multiplication table of a number as a list.

def multi_num(n):
    l= []
    for i in range (1,11):
        num = n * i
        l.append(num)
    return l
n = int(input("Enter Num: "))
checknum=multi_num(n)
print(checknum)
# Note:
# This solution is written by me.
# I only took hints/formulas from ChatGPT.
# The syntax, logic implementation, and code structure are my own.     
    
#14 Create a function that returns all factors of a number as a list.

def factors(n):
    l = []
    
    for i in range(1,n+1):
        if n % i ==0:
            l.append(i)
    return l
n = int(input("Enter Num: "))
checknum = factors(n)
print(checknum)

#15 Create a function that returns the count of vowels in a string.

vowels = ("aeiou")

def vowel_check(ch):
    check=0
    for i in ch:
     if i in vowels:
        check +=1

    return check

ch = input("Enter Sentense: ")
check_sentense_vowel=vowel_check(ch)
print(check_sentense_vowel)

#16 Create a function:
'''employee(name, salary=50000)
Print both values.
Call it:
once using the default salary
once by passing your own salary'''

#Problem 16
def employee(name,salary=50000):
    print(name,salary)

employee("Shanzail") # By Deafult Call Argument 
employee("Shanzail",100000) # By Key Call Arugument

#17 reate a function:
'''person(name, city="Hyderabad", country="Pakistan")
Call it using keyword arguments in a different order.'''
#Problem 17
def person(name,city="Hyderabad",country="Pakistan"):
    print(name)
    print(city , country)

person("Muhammad Shanzail")  # By Deafult Call Argument  
person("\nMuhammad Shanzail","Karachi","America") # By Key Call Arugument 

#18 Create a function:
'''power(base, exponent=2)
Return the result.
Call it:
once with default exponent
once with exponent = 3'''
#Problem 18
def power(base,exponent=2):
    print(base**exponent)

power(5)
power(5,3)

#19 Create a global variable named course.
'''Print it: Inside the Function
outside the function'''
#Problem 19
course = "Python Programming"

def details(name):
    print(name)
    print(course) # Inside the Function
details("Shanzail")
print(course) # Outside the Function

#20 Create two functions.
'''Each should have a local variable called message.
Print both messages.'''
# Problem20
def function1(name):
    message="This is local variable 1"
    print(name)
    print(message)

def function2(name):
    message="This is Local variable 2 "
    print(name)
    print(message) 

function1("Shanzail")
function2("Ali")

#21 Create a function that returns whether a number is Prime. 
def prime_num(n):
    for i in range(2,n):
        if n % 2==0:
            return("Not Prime")
        else:
            return("Prime Num")

n = int(input("Enter Num: "))
checknum=prime_num(n)
print(checknum)

# 22 Create a function that returns whether a string is a Palindrome.
'''Examples:
madam → True
level → True
python → False'''
#Problem 22

def palindrome(word):
     if word == word[::-1]:
          return("True")
     else:
          return("False")
word = input("Enter Word: ")    
check_word=palindrome(word)
print(check_word)

#23 Create a function that returns the largest number from a list.
'''Example:
numbers = [12, 45, 7, 89, 32]'''
#Problem 23
numbers = [12, 45, 7, 89, 32]
def largest():
    largest = numbers[0]
    for i in numbers:
        if i > largest:
          largest=i
    return largest

check_num=largest()
print(check_num)

#24 Create a function that returns the second largest number from a list.
'''Example:
[10, 30, 80, 45, 90]'''
#Problem 24
num = [10, 30, 80, 45, 90]

def sec_largest():
    largest_num = num[0]
    sec_largest_num = num[0]
    for i in num:
        if i > largest_num:
            sec_largest_num = largest_num
            largest_num = i
        elif i > sec_largest_num and i < largest_num:
            sec_largest_num = i
    return sec_largest_num

checknum = sec_largest()
print(checknum)
# Chatgpt se madad li hay formula ke liyesyntax me nh shi kia tha logic pouchne ke liye

# 25 Create a function:
'''employee_salary(name, basic_salary, bonus=5000)
The function should:
Calculate:
Total Salary = Basic Salary + Bonus

Return:
Name
Basic Salary
Bonus
Total Salary

Then print:
========== EMPLOYEE REPORT ==========
Name          :
Basic Salary  :
Bonus         :
Total Salary  :
====================================='''

#Problem 25

def employee_salaray(name,salary,bonus=5000):
    total_salary = salary + bonus
    print("\n========== EMPLOYEE REPORT ==========")
    print("Name: ",name)
    print("Basic Salary: ",salary)
    print("Bonus: ",bonus)
    print("Total Salary: ",total_salary)
    print("=====================================")
    return(name,salary,bonus,total_salary)

check_employee_salaray= employee_salaray("Ali",60000)
print(check_employee_salaray)

# TimeTaken = 50Mint
# Day 9 Score
# Overall Rating: 9.4/10 ⭐