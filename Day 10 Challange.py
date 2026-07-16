                            #  100 Days Python Challange 
                        # Day Ten(10) Python 25 Questions 
print("\t\t\t\t\tDev.Shanzail Backend Developer") # Name And Role

#1 Create a function is_even(num) that returns True if the number is even, otherwise False.

def is_even(num):
    if num % 2 ==0:
        return True
    else:
        return False
num = int(input("Enter num: "))
check_num_even= is_even(num)
print(check_num_even)

#2 Create a function is_odd(num) that returns True if the number is odd, otherwise False.

def is_odd(num):
    if num%2 != 0:
        return True
    else:
        return False
num = int(input("Enter Num: "))    
check_num_odd=is_odd(num)
print(check_num_odd)

#3 Create a function circle_area(radius) that returns the area of a circle. (Use 3.14)

def circle_area(radius):
    area = 3.14 * (radius ** 2)
    return(area)

radius=int(input("Enter Radius: "))
check_area=circle_area(radius)
print(check_area)

#4 Create a function rectangle_perimeter(length, width) that returns the perimeter.

def rectangle_perimeter(length , width):
    perimeter = 2 * (length + width)
    return(perimeter)
length=int(input("Enter Length: "))
width=int(input("Enter Width: "))
check_perimter=rectangle_perimeter(length,width)
print("Perimeter of Rectangle is: ",check_perimter)

#5 Create a function cube(num) that returns the cube of a number.
def cube_num(num):
    return(num*num*num)
num=int(input("Enter Num: "))
check_cube=cube_num(num)
print("Cube of Num is: ",check_cube)

#6 Create a function largest_of_four(a, b, c, d) that returns the largest number
def largest_num(a,b,c,d):
    if a>=b and a>=c and a>=d:
        return(a)
    elif b>=a and b>=c and b>=d:
        return(b)
    elif c>=a and c>=b and c>=d:
        return(c)
    else:
        return(d)
a= int(input("Enter Num a: "))    
b= int(input("Enter Num b: "))    
c= int(input("Enter Num c: "))    
d= int(input("Enter Num d: "))    
check_largest_num=largest_num(a,b,c,d)
print(check_largest_num)

#7 Create a function smallest_of_four(a, b, c, d) that returns the smallest number.
def smallest_num(a,b,c,d):
    if a<=b and a<=c and a<=d:
        return(a)
    elif b<=a and b<=c and b<=d:
        return(b)
    elif c<=a and c<=b and c<=d:
        return(c)
    else:
        return(d)
a = int(input("Enter Num a: "))
b = int(input("Enter Num b: "))
c = int(input("Enter Num c: "))
d = int(input("Enter Num d: "))

check_num = smallest_num(a,b,c,d)
print(check_num)

#8 Create a function count_characters(text) that returns the total number of characters.
def count_character(text):
    length=(len(text))
    return length
word = input("Enter Word: ")
check_word=count_character(word)
print(check_word)

#9 Create a function count_words(sentence) that returns the total number of words.

def count_word(sentense):
    check_words = sentense.split()
    return len(check_words)

sentense=input("Enter Sentense here: ")
output=count_word(sentense)
print(output)

#10 Create a function reverse_string(text) that returns the reversed string.

def reverse_string(text):
    reverse = text[::-1]
    return reverse

text = input("Enter text here: ")
check = reverse_string(text)
print(check)

#11 Create a function is_uppercase(char) that returns True if the character is uppercase.
def is_uppercase(char):
    check_upper = char.upper()
    if check_upper == char:
        return True
    else:
       return False

word = input("Enter Word: ")
check=is_uppercase(word)
print(check)

#12 Create a function is_lowercase(char) that returns True if the character is lowercase.

def lowercase(char):
    if char.islower():
        return True
    else:
       return False
char=input("Enter Word: ")
check= lowercase(char)
print(check)

#13 Create a function sum_list(numbers) that returns the sum of all elements in a list
num = [10,20,30,40]
def  sum_list(num):
    sum_num= sum(num)
    return(sum_num)

check=sum_list(num)
print(check)

#14 Create a function average_list(numbers) that returns the average of the list.
num = [10,20,30,40] 
def average_list(num):
    total = sum(num)
    average_num = total/(len(num))
    return(average_num)

check = average_list(num)
print(check)

#15 Create a function maximum_list(numbers) that returns the largest value from a list without using max().

numbers = [10,3,42,50]

def maximum_list(numbers):
    largest_num = numbers[0]
    for i in numbers:
        if i > largest_num:
              largest_num = i
    return largest_num

check = maximum_list(numbers)
print(check)

#16 Create a function minimum_list(numbers) that returns the smallest value from a list without using min().
numbers = [10,3,42,50]
def minimum_list(numbers):
    smallest_num = numbers[0]
    for i in numbers:
        if i < smallest_num:
            smallest_num = i
    return smallest_num

check= minimum_list(numbers)
print(check)

#17 Create a function count_even(numbers) that returns how many even numbers are in a list.

l = [2,4,5,6,10,8]

def count_even(l):
    count_even_num = 0
    for i in l:
        if i % 2==0:
            count_even_num +=1
    return count_even_num
            

check = count_even(l)
print(check)

#18 Create a function count_odd(numbers) that returns how many odd numbers are in a list.
l = [2,4,5,6,10,8,11]

def count_odd(l):
    count_odd_num = 0
    for i in l:
        if i % 2 != 0 :
            count_odd_num +=1
    return(count_odd_num)

check = count_odd(l)
print(check)

#19 Create a function table(number) that returns the multiplication table (1–10) as a list.

def table(number):
    l = []
    for i in range(1,11):
        check =(f"{number} * {i} = {number*i}")
        l.append(check)
    
    return l
number = int(input("Enter Num for Multiplication: "))
check = table(number)
print(check)

#20 Create a function factorial(num) that returns the factorial.

def factorial_num(num):
    factorial = 1
    for i in range(1,num):
        factorial = factorial * i
    return (factorial)

num = int(input("Enter Num: "))
check = factorial_num(num)
print("The Factorial of Num is, ",check)

#21 Create a function prime(num) that returns True if the number is prime, otherwise False.

def prime_num(num):
    for i in range(2,num):
        if num % i == 0:
         return False
        num < 2
    else:
      return True
num = int(input("Enter Num: "))
check = prime_num(num)
print(check)

#22 Create a function fibonacci(n) that returns the first n Fibonacci numbers as a list.

def fibonacci_num(n):
    result=[]
    a = 0
    b = 1
    for i in range(n):
        result.append(a)
        next_num = a + b
        a = b
        b = next_num
    return result

n = int(input("Enter Num: "))
check = fibonacci_num(n)
print(check)

#23 Create a function student(name, marks) where marks is a list of 5 subjects. Return:
'''Total
Average
Grade'''
#Problem 23
def student(name,marks):
    total = sum(marks)
    average = total/len(marks)
    if average>=90:
        garde="A+"
    elif average>=80:
        garde="A"
    elif average>=70:
        garde ="B"
    elif average>=60:
        garde = "C"
    else:
        garde="fail"
    return (name,total,average,garde)

checkresult=student("Shanzail",[45,49,89,98,78])
print(checkresult)

#24 Create a function calculator
# (a, b, operation) that performs +, -, *, /, %, ** based on the operation.

def calculator(a,operation,b):
    if operation == "+":
        print("Addition of a and b is: ",a+b)
    elif operation == "-":
        print("Subtraction of a and b is: ",a-b)
    elif operation == "*":
        print("Multiplication of a and b is: ",a*b)
    elif operation == "/":
        print("Division of a and b is: ",a/b)
    elif operation == "%":
        print("Modulus of a and b is: ",a%b)
    elif operation == "**":
        print("Exponent(Power) of a and b is: ",a**b)
    else:
        print("Invalid O")



    
a = int(input("Enter num1: "))
operation = input("Enter operation: ")
b = int(input("Enter num2: "))    

calculator(a,operation,b)

#25 Create a function:
'''bank_account(name, account_number, balance, deposit=0, withdraw=0)
The function should:
Update the balance after deposit.
Subtract the withdraw amount (only if balance is sufficient).
Return:
Name
Account Number
Deposit
Withdraw
Final Balance

Print the result like:
========== BANK ACCOUNT ==========
Name            :
Account Number  :
Deposit         :
Withdraw        :
Final Balance   :
=================================='''
#Problem 25
def bank_account(name,account_num,balance,deposit=0,withdraw=0):
   # Doposit
   balance = balance + deposit
   # Withdraw
   if balance >= withdraw:
     balance= balance - withdraw
   else:
    print("Blance is Low")
    
   return(name,account_num,deposit,withdraw,balance)

name = input("Enter yours GoodName: ")
account_num = int(input("Enter your AccountNum: "))
balance = int(input("Enter your balance: "))
deposit = int(input("Enter your deposit ammount: "))
withdraw = int(input("Enter withdraw ammount: "))


result=bank_account(name,account_num,balance,deposit,withdraw)

name , account_num , deposit , withdraw , finalbalance = result
print(result)

print("========== BANK ACCOUNT ==========")
print("Name: ",name)
print("Account Number: ",account_num)
print("Deposit: ",deposit)
print("Withdraw: ",withdraw)
print("Final Balance:",finalbalance)
print("==================================")

# TimeTaken = 70Mint
# ⭐ Day 10 Rating
# Day 10 Overall Score: 9.8/10 ⭐⭐⭐⭐⭐