                        #  100 Days Python Challange 
                        # Day Twelve(12) Python 25 Questions 
print("\t\t\t\t\tDev.Shanzail Backend Developer") # Name And Role

#1 Create a function countdown(n) that prints from n to 1 using recursion
def countdown(n):

    if n ==0:
     return 
    print(n)
    countdown(n-1)

n = int(input("Enter Number: "))
countdown(n)

#2 Create a function countup(n) that prints from 1 to n using recursion.
def countup(current,n):
    if current > n:
     return
    print(current)
    countup(current + 1,n)
    
# n = int(input("Enter Number: "))
countup(1,6)

#3 Create a function sum_n(n) that returns the sum of numbers from 1 to n

def sum_n(n):
    if n == 0:
        return 0
    return n + sum_n(n-1)
n = int(input("Enter Numbers: "))
check =sum_n(n)
print(check)

#4 Create a function factorial(n) using recursion.
def factorial(n):
    if n == 0:
        return 1
    
    return n * factorial(n-1)
n = int(input("Enter Num: "))
check = factorial(n)
print(f"The Factorial of Num is {check}")

#5 Create a function power(base, exponent) using recursion.

def power(base,exponent):
    if exponent == 0:
        return 1
    
    return base*power(base , exponent-1)


base = int(input("Enter Num: "))
exponent = int(input("Enter Exponent(power): "))

check= power(base,exponent)
print(f"The Num {base} with Power of {exponent} is {check}")

#6 Create a function print_even(n) that prints all even numbers from n to 0.

def even(n):

    if n < 0:
        return
    
    if n % 2 == 0:
        print(n)
    
    even(n-1)
n = int(input("Enter Num: "))
even(n)

#7 Create a function print_odd(n) that prints all odd numbers from n to 1.

def odd(n):
    if n < 1:
        return
    if n % 2 != 0:
        print(n)
    odd(n-1)
n = int(input("Enter Num: "))
odd(n)

#8 Create a function count_digits(n) using recursion.

def count_digit(n):
    if n==0:
        return 0
    
    return 1 + count_digit(n // 10)

n = int(input("Enter Num: "))
check = count_digit(n)
print(check)
         
#9 Create a function reverse_string(text) using recursion.
def reverse_string(text):
    if text == "":
        return ""
    
    return reverse_string(text[1:]) + text[0]

text = input("Enter Text: ")
check =reverse_string(text)
print(check)

#10 Create a function sum_digits(n) using recursion

def sum_digit(n):
    if n == 0:
        return 0
    return (n % 10) + sum_digit(n // 10)

n = int(input("Enter Num: "))
check = sum_digit(n)
print(check)

#11 Find the product of numbers from 1 to n using recursion.

def product_num(n):
    if n == 1:
        return 1
    return n * product_num(n-1)

n = int(input("Enter Num: "))
check = product_num(n)
print(f"The Product of Num is {check}")

#12 Find the nth Fibonacci number using recursion
def fibonacci_num(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci_num (n-1) + fibonacci_num(n-2)

n= int(input("Enter Number: "))
check = fibonacci_num(n)
print(check)

#13 Print the first n Fibonacci numbers using recursion.
def first_fibonacci_number(n,n1,n2):
    if n == 0:
        return 
    print(n1)
    return first_fibonacci_number(n-1,n2,n1+n2)


n = int(input("Enter Num: "))
n1 = int(input("Enter num2: "))
n2 = int(input("Enter Num3: "))
first_fibonacci_number(n,n1,n2)

#14 Check whether a string is a palindrome using recursion
def is_palindrome(text):
    if len(text) <= 1:
        return True
    
    if text[0] != text[-1]:
        return False
    
    return is_palindrome(text[1:-1])

text = input("Enter Text here: ")
check = is_palindrome(text)
print(check)

#15 Count vowels in a string using recursion
vowel = ("aeiouAEIOU")
def count_vowel(text):
    if text == "":
        return 0
    if text[0] in vowel:
        return 1 + count_vowel(text[1:])
    else:
        return count_vowel(text[1:])
text = input("Enter Text: ")
print(count_vowel(text))

#16 Find the maximum element in a list using recursion.
l1 = [23,56,70,34,58]
def maximum(l1):
    if len(l1) == 1:
        return l1[0]
    maximum = max(l1[1:])

    if l1[0] > maximum:
        return l1[0]
    else:
        return maximum
    
print(maximum(l1))

#17 Find the minimum element in a list using recursion.
l1 = [23,56,70,34,58]

def minimum(l1):
    if len(l1) == 1:
        return l1[0]
    minimum = min(l1[1:])

    if l1[0] < minimum:
        return l1[0]
    else: 
        return minimum
    
print(minimum(l1))

#18 Sum all elements of a list using recursion.
l1 = [4,1,5,3,2]
def sum_list(l1):
    if l1 == []:
        return 0
    
    return l1[0] + sum_list (l1[1:])

print(sum_list(l1))

#19 Count occurrences of a number in a list using recursion. 
numbers = [2,5,2,3,2]
target = int(input("Enter Target Num to check occurence:"))
def occourence_num_list(numbers,target):
    if numbers == []:
        return 0
    
    if numbers[0] == target:
        return 1 + occourence_num_list(numbers[1:],target)
    else:
        return occourence_num_list(numbers[1:],target)
    
check=(occourence_num_list(numbers,target))
print(f"The num occour in list is {check}")

#20 Reverse a list using recursion.
numbers = [2,5,2,3,2]
def reverse_list(numbers):
    if numbers == []:
        return []
    return reverse_list(numbers[1:]) + [numbers[0]]

print(reverse_list(numbers))

#21 Find the GCD of two numbers using recursion

def gcd(a,b):
    if b == 0:
        return a 
    
    remainder = a % b
    
    return gcd(b, remainder)
a= int(input("Enter Num: "))
b= int(input("Enter Num: "))
check = gcd(a,b)
print(check)

#22 Find the LCM of two numbers using recursion.

def lcm(a,b, multiple):

    # multiple = max(a,b)
    if multiple % a == 0 and multiple % b == 0:
        return multiple
    
    return lcm(a,b,multiple +1)


a = int(input("Enter Num: "))
b = int(input("Enter Num: "))
multiple = max(a,b)
check = lcm(a,b,multiple)
print(f"The Lcm of {a} and {b} is {check}")

#23 Convert a decimal number to binary using recursion. 

def decimal_num_binary(num):
    if num == 0:
        return ""
    divison = str(num % 2)
    return decimal_num_binary(num // 2) + divison

num = int(input("Enter Num: "))
check = decimal_num_binary(num)
print(f"The Decimal num {num} in Binary is {check}")

#24 Calculate base^exponent without using ** (recursion only).

def base_exponent(a,b):
    if b == 0:
        return 1
    
    return a * base_exponent (a,b -1)

a = int(input("Enter Base: "))
b = int(input("Enter Exponent: "))

check = base_exponent(a,b)
print(f"The Base {a} with Exponent {b} is {check}")

#25 ⭐ Final Challenge
'''Create a recursive function:
student_report(marks)

It should recursively calculate:
Total Marks
Average
Highest Marks
Lowest Marks

Return all four values and print a formatted report'''
#Problem 25
def calculate_total(marks): # Calculate Total Marks 
    if marks == []:
        return 0
    return marks[0] + calculate_total(marks[1:])

def find_highest(marks): # Find Highest Marks
    if len(marks) == 1:
        return marks[0]
    
    highest = find_highest(marks[1:])
    if marks[0] > highest:
        return marks[0]
    else:
        return highest
    
def find_lowest(marks): # Find Lowest Marks
    if len(marks) == 1:
        return marks[0]
    lowest = find_lowest(marks[1:])
    if marks[0] < lowest:
        return marks[0]
    else:
        return lowest 
    
def student_report(marks):

    total = calculate_total(marks)

    highest = find_highest(marks)

    lowest = find_lowest(marks)

    average = total / len(marks)
    
    return total , highest , lowest , average
    
marks = []
mark1 = int(input("Enter Marks1: "))
marks.append(mark1)
mark2 = int(input("Enter Marks2: "))
marks.append(mark2)
mark3 = int(input("Enter Marks3: "))
marks.append(mark3)
mark4 = int(input("Enter Marks4: "))
marks.append(mark4)
check = student_report(marks)
print(check)

# TimeTaken = 109 Mint 

# 📊 Day 12 Rating
# Correctness: 9.4/10
# Logic Building: 9.8/10
# Recursion Understanding: 9.3/10
# Overall: 9.5/10 (Excellent) ⭐

# 👍 Sab se achi baatein
# ✅ Base case almost har function me sahi hai.
# ✅ Recursive call sahi jagah use ki hai.
# ✅ String recursion samajh aa rahi hai.
# ✅ List recursion bhi achi hai.
# ✅ GCD, LCM, Binary conversion jaise difficult questions khud implement kiye.
# ✅ Final challenge ko multiple recursive functions me divide kiya (professional approach).

# Final Estimate: # Dev.Shanzail: 97% 💪 # ChatGPT: 3% 🤝


   

    

    
    

    




