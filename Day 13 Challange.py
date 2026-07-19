                            #  100 Days Python Challange 
                        # Day Thirteen(13) Python 25 Questions 
print("\t\t\t\t\tDev.Shanzail Backend Developer") # Name And Role

#1 Create a function sum_even(n) using recursion.
# Return the sum of all even numbers from 1 to n.

def sum_even(n):

    if n==0:
     return 0

    if n % 2 == 0:
       return n + sum_even(n-1)
    else:
       return sum_even(n-1)

n = 6
check= sum_even(n)
print(f"The Sum of {n} Even numbers is {check}")

#2 Create a function sum_odd(n) using recursion.
# Return the sum of all odd numbers from 1 to

def sum_odd(n):

    if n==0:
        return 0
    
    if n % 2 != 0:
        return n + sum_odd(n-1)
    else:
        return sum_odd (n-1)

n = int(input("Enter Num: "))
check = sum_odd(n)
print(f"The Sum of Odd Num{n} is {check}")

#3 Create a function countdown_even(n) using recursion.
# Print only even numbers from n to 0.

def count_down_even(n):
    if n < 0:
        return
    
    if n % 2== 0:
        print(n)

    count_down_even (n - 1)

n = int(input("Enter Num: "))
(count_down_even(n))

#4 Create a function countup_odd(n) using recursion.
# Print only odd numbers from 1 to n.

def countup_odd(n):
    if n < 0:
     return
    
    countup_odd (n-1)
    
    if n % 2 != 0:
     print(n)
    

n = int(input("Enter Num: "))
countup_odd(n)

#5 Create a function multiply(a, b) using recursion. (Do not use *.)

def multiply (a,b):

    if b == 0:
        return 0
    
    return a + multiply(a , b-1)

a = int(input("Enter Num1: "))
b = int(input("Enter Num2: "))
check = multiply(a,b)
print(f"The Num1{a} Multiply By Num2{b}  is {check}")

#6 Create a function count_characters(text) using recursion.Return total characters.

def count_characters(text):

    if text == "":
        return 0
    
    return 1 + count_characters(text[1:])

text = input("Enter Text: ")
check = count_characters(text)
print(f"The Text You Enter Count Characters is {check}")

#7 Create a function count_uppercase(text) using recursion.Return total uppercase letters.

def count_uppercase(text):

    if text == "":
        return 0
    
    if text[0].isupper():
     return 1 + count_uppercase(text[1:])
    else:
       return count_uppercase(text[1:])
    
text = input("Enter Text: ")
Check = count_uppercase(text)
print(Check)

#8 Create a function count_lowercase(text) using recursion.Return total lowercase letters.

def count_lowercase(text):
    if text == "":
        return 0
    
    if text[0].islower():
        return 1 + count_lowercase(text[1:])
    else:
        return count_lowercase(text[1:])
    
text = input("Enter Text: ")
check = count_lowercase(text)
print(check)

#9 Create a function count_special(text) using recursion.Return total special characters.

def count_special(text):
    if text == "":
        return 0
    
    if not text[0].isalpha() and not text[0].isdigit():
        return 1 + count_special(text[1:])
    else:
        return count_special(text[1:])

text = input("Enter Text: ")
check = count_special(text)
print(check)

#10 Create a function replace_spaces(text) using recursion./Replace every space with _.
 
def replace_spaces(text):
    if text == "":
        return ""
    
    if text[0] == " ":
        return "_" + replace_spaces(text[1:])
    else: 
        return text[0] + replace_spaces(text[1:])

text = input("Enter Text: ")
check = replace_spaces(text)
print(f"Your Text After Replace by space into '_' {check}")

# 11 Create a function remove_character(text, ch) using recursion. Remove all occurrences of a character.

def remove_character (text , ch):

    if text == "":
        return ""
    
    if text[0] == ch:
        return remove_character(text[1:], ch)
    else: 
        return text[0] + remove_character(text[1:] , ch)
    
text = input("Enter text: ")
ch = input("Enter Ch: ")
check = remove_character(text,ch)
print(check)

#12 Create a function count_occurrences(text, ch) using recursion. Return how many times a character appears.

def count_occurrences(text,ch):

    if text == "":
        return 0
    
    if text[0] == ch:
        return 1 + count_occurrences (text[1:],ch)
    else:
        return count_occurrences(text[1:],ch)
    
text = input("Enter Text: ")
ch = input("Enter ch: ")
check = count_occurrences(text,ch)
print(check)

#13 Create a function reverse_list(numbers) using recursion./ Without using slicing.
l1 = [10,20,30,40,50]
def reverse_list(l1):
    if len(l1) == 1:
        return l1
    
    remove = l1.pop()
    
    return [remove] + reverse_list(l1)

check = reverse_list(l1)
print(check)

#14 Create a function list_length(numbers) using recursion./ Without using len()

numbers = [10,45,67,86]
def list_length(numbers):
    if numbers == []:
        return 0
    
    remove_one_element = numbers.pop()

    return 1 + list_length(numbers)

check = list_length(numbers)
print(check)

#15 Create a function list_average(numbers) using recursion. / Do not use sum().
num = [10,30,20]

def calculate_total(num):
    if num == []:
        return 0
    
    remove_one_element = num.pop()

    return remove_one_element + calculate_total(num)

def list_average(num):
    total_element = len(num)

    total = calculate_total(num)
    average = total / total_element
    return average

check = list_average(num)
print(f"The Average of List is {check}")

#16 Create a function find_smallest(numbers) using recursion. / Without using min().
num = [10,67,5,15]
def find_smallest(num):
    if len(num) == 1:
        return num[0]
    
    smallest = find_smallest(num[1:])

    if num[0] < smallest:
        return num[0]
    else:
        return smallest
    
check = find_smallest(num)
print(f"The Smallest of List {num} is {check}")

#17 Create a function find_second_largest(numbers) using recursion. 
l1 = [23,24,26,25,22]

def find_sec_largest(l1): # Function 

    if len(l1) == 2:  # Base Case
        
        if l1[0] > l1[1]: # Base With Conditions
            return l1[0],l1[1]
        else:
            return (l1[1],l1[0])
        
    largest , sec_largest = find_sec_largest(l1[1:])

    first = l1[0]

    if first > largest:
         sec_largest = largest
         largest = first
    else:
        if first > sec_largest:
            sec_largest = first

    return largest , sec_largest

largest , sec_largest = find_sec_largest(l1)
print(f"The Second_Largest Num in List is {sec_largest}")

#18 Create a function find_second_smallest(numbers) using recursion.
num = [20,30,40,60]
def find_second_smallest(num):

    if len(num) == 2:
        
        if num[0] < num[1]:
            return num[0] , num[1]
        else:
            return num[1] , num[0]
        
    smallest , sec_smallest = find_second_smallest(num[1:])

    first = num[0]

    if first < smallest:
        sec_smallest = smallest
        smallest = first

    else:
        if first < sec_smallest:
            sec_smallest = first
    
    return smallest , sec_smallest

smallest , sec_smallest = find_second_smallest(num)
print(f" The Second Smallest of List is {sec_smallest}")

#19 Create a function is_sorted(numbers) using recursion. Return True or False.
numbers = [23,45,87,6]
def is_sorted(numbers):

    if len(numbers) <= 1:
        return True
    
    first = numbers[0]
    second = numbers[1]

    if first > second:
        return False
    
    return is_sorted(numbers[1:])

check = is_sorted(numbers)
print(check)

#20 Create a function count_positive(numbers) using recursion.
numbers = [23,-977,87,54,-87,9]
def count_postitive(numbers):
    if numbers == []:
        return 0
    
    first = numbers[0]

    if first > 0:
        return 1 + count_postitive(numbers[1:])
    else:
        return count_postitive(numbers[1:])
    
check = count_postitive(numbers)
print(f"{numbers} Total Positive Numbers is {check}")

#21 Create a function count_negative(numbers) using recursion.
numbers = [23,-977,87,54,-87,9]

def count_negative(numbers):
    if numbers == []:
        return 0 
    
    first = numbers[0]

    if first < 0:
        return 1 + count_negative(numbers[1:])
    else:
        return count_negative(numbers[1:])
    
check = count_negative(numbers)
print(check)

#22 Create a function decimal_to_octal(n) using recursion.

def deicmal_octal(n):
    if n < 8:
        return str(n)
    remainder = (n % 8)
    return deicmal_octal(n// 8) + str(remainder)

n = (int(input("Enter Decimal to Convert into Octal Num: ")))
check = deicmal_octal(n)
print(f"The Decimal Num {n} in Octal Num is {check}")

#23 Create a function decimal_to_hexadecimal(n) using recursion. (Without using hex().)

def decimal_hexa_decimal(n):
    hex_digits = "0123456789ABCDEF"

    if n < 16:
        return hex_digits[n]
    
    remainder = n % 16

    return decimal_hexa_decimal(n//16) + str(remainder)

n = int(input("Enter Decimal Num to Convert Into Hexa_Decimal: "))
check = decimal_hexa_decimal(n)
print(f"{n} Decimal num into Hexa_Decimal is {check}")

#24 Create a recursive function digit_product(n).

def digit_product(n):
    if n < 10:
        return n
    
    return (n % 10 ) * digit_product(n // 10)

n = int(input("Enter Num: "))
check = digit_product(n)
print(check)

#25 ⭐ 25. Final Challenge
'''Create:
student_analysis(marks)
Using recursion only.

Return:
Total Marks
Average
Highest Marks
Lowest Marks
Number of Passed Subjects (≥40)
Number of Failed Subjects (<40)

Print:
========== STUDENT ANALYSIS ==========
Total:
Average:
Highest:
Lowest:
Passed Subjects:
Failed Subjects:
======================================'''
# Problem 25 
marks = [60,65,29,76]
def calculate_total(marks):  # Function Calculate Total Marks 
    if marks == []:
        return 0
    first_marks = marks[0]
    return first_marks + calculate_total(marks[1:])

def calculate_average(marks): # Function Calculate Average Marks
    total = calculate_total(marks)
    average = total / len(marks)
    return average 

def find_highest(marks):  # Function Calculate Highest Marks 
    if len(marks) == 1:
        return marks[0]
    
    first_mark = marks[0]
    highest = find_highest(marks[1:])

    if first_mark > highest:
        return first_mark
    else:
        return highest

def find_lowest(marks): # Function Calculate Lowest Marks 
    if len(marks) == 1:
        return marks[0]
    
    first_mark = marks[0]
    lowest = find_lowest(marks[1:])

    if first_mark < lowest:
        return first_mark
    else:
        return lowest
    
def count_passed(marks):  # Function Calculate Count Passed Marks 
    if marks == []:
        return 0 
    
    first_mark = marks[0]

    if first_mark >= 40:
        return 1 + count_passed(marks[1:])
    else:
        return count_passed(marks[1:])

def count_failed(marks):  # Function Calculate Count Failed Marks 
    if marks == []:
        return 0
    
    first_mark = marks[0]
    if first_mark < 40:
        return 1 + count_failed(marks[1:])
    else:
        return count_failed(marks[1:])
    
def student_analysis(marks): # Final Function Student Analysis

    total = calculate_total(marks)
    average = calculate_average(marks)
    highest = find_highest(marks)
    lowest = find_lowest(marks)
    passed = count_passed(marks)
    failed = count_failed(marks)

    return total , average , highest , lowest , passed , failed 

total , average , highest , lowest , passed , failed = student_analysis(marks)
# check = student_analysis(marks)
# print(check)

print("========== STUDENT ANALYSIS ==========")
print("Total:" ,total )
print("Average:" , average)
print("Highest:" , highest)
print("Lowest:" , lowest)
print("Passed Subjects:" , passed)
print("Failed Subjects:" , failed)
print("======================================" , )


# TimeTaken = 132 Mint
# ⭐ Day 13 Overall Rating: 9.3/10
# Breakdown:
# Recursion Understanding: 9.5/10
# Logic Building: 9.5/10
# Implementation: 9/10
# Problem Solving: 9.5/10

# Feedback By chatgpt
# Ab tum recursion ke baad 
# easily searching algorithms, sorting algorithms aur backtracking 
# samajh sakte ho.





    

    
        
        






