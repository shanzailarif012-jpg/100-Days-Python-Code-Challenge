                        # 100 Days Python Challange 
                        # Day Six(6) Python 25 Questions 
print("\t\t\t\t\tDev.Shanzail Backend Developer") # Name And Role

#1 Take your full name as input and print:

'''Original Name
Uppercase
Lowercase
Total Characters'''
# problem 1 

name = input("Enter Name: ")

print(name)
print(name.upper())
print(name.lower())
print(len(name))

#2 Take a number as input and print its:
'''Integer type
Float type
String type'''
# problem 2 
num = int(input("Enter Num: "))

print(num,type(num))
print(float(num),type(float(num)))
print(str(num),type(str(num)))

#3 take a sentence and print every character on a new line using a loop.

sentense = input("Enter Sentense: ")

for i in sentense:
    print(i)

#4 Take a word and count how many vowels it contains.

vowels = ("a","e","i","o","u")
check = 0
word = input("Enter word: ")

for ch in word:
    if ch in vowels:
        check = check + 1
print(check)

#5 Take a sentence and reverse every word individually.

word = input("Enter Word: ")

sentense = word.split()
reverse_word = [word[::-1] for word in sentense]
final=" ".join(reverse_word)
print(final)  # ye bht he mushkil tha mene slicing ki madad se kiya tha ye muje nh ata tha taqreban mene ye claude ki madad se kiya hay 75 percent code 
                # Note Formula mene claude se liya hay bs placement bi 50percent

#6 Create a list of 10 numbers and print:
'''Maximum number
Minimum number
Sum of all numbers'''
# Problem 6 
l = [1,4,67,87,5,69,100,14,16,55]
print(max(l))
print(min(l))
print(sum(l))

#7 Take 5 numbers from the user and store them in a list. print the list.

l=[]

l1=int(input("Enter num1: "))
l.append(l1)
l2=int(input("Enter num2: "))
l.append(l2)
l3=int(input("Enter num3: "))
l.append(l3)
l4=int(input("Enter num4: "))
l.append(l4)
l5=int(input("Enter num5: "))
l.append(l5)

print(l)

#8 Create a tuple of 12 months and print only the summer months:
'''June
July
August'''
# Problem 8

months = ("Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec")
print(months[5])
print(months[6])
print(months[7])

#9 Create a dictionary of 5 students and their marks. print only the students who scored above 80.
marks = 0
students = {
    "Shanzail":76,
    "Ali":87,
    "Haris":54,
    "Sara":87,
    "Yahya":65
}

for key, value in students.items():
    if value > 80:
        print(key)

#10 Create two sets:
'''A = {1,2,3,4,5}
B = {4,5,6,7,8}
print:
Union
Intersection
Difference (A - B)'''
# Problem 10

A = {1,2,3,4,5}
B = {4,5,6,7,8}
print("Set A",A)
print("Set B",B)
print("Union of A and B is: ",A.union(B))
print("Intersection of A and B is: ",A.intersection(B))
print("Diffeence of A and B is: ",A.difference(B))

#11 Take a number and check whether it is:
'''Single digit
Double digit
More than two digits'''
#Problem 11
num = int(input("Enter num: "))


if abs(num)<10:
     print("Single Digit")
elif 10<= abs(num)<100:
    print("Double Digit")
else:
     print("More then two digit") # Note Formula mene claude se liya hay

#12 Take three angles of a triangle.Check whether the triangle is valid.

a1 = int(input("Enter Angle1: "))
a2 = int(input("Enter Angle2: "))
a3 = int(input("Enter Angle3: "))

if a1 + a2 + a3 == 180 and a1 > 0 and a2 > 0 and a3 > 0:
    print("Valid Angle")
else:
    print("Not Valid") # Note Formula mene claude se liya hay

#13 take the price of a product.
'''Apply:
20% discount if price > 5000
10% discount if price > 2000
No discount otherwise
print the final price.'''
#Problem 13

price = int(input("Enter Price: "))
print(price)
# price * (1 - discount_percent / 100) # Fromula For Dsicount
if price>5000:
    price = price * (1- 20 / 100)
    print("After 20% price is:",price)
elif price>2000:
    price = price * (1- 10 / 100)
    print("After 10% price is: ",price)
else:
    print("No Discount on this price") # Note Formula mene claude se liya hay

#14 Take a character and check whether it is:
'''Alphabet
Number
Special Symbol'''
# Problem 14

character = input("Enter Character: ")

if character.isalpha():
    print("Alphabet")
elif character.isdigit():
    print("Number")
else:
    print("Special Symbol") # Note Formula mene claude se liye hay 

#15 Take two numbers and print:
'''Greater
Smaller
Equal'''
#Problem 15

num1 = int(input("Enter num1: "))
num2 = int(input("Enter num2: "))

if num1>num2:
    print("Greater Num")
elif num1<num2:
    print("Smaller")
elif num1==num2:
    print("Both Equal")

#16 print the first 20 multiples of 3.

for i in range(1,21):
    print(f"{3} * {i} = {3*i}")
   

#17 Find the sum of odd numbers from 1 to 100.
total = 0
for num in range(1,101):
     if num % 2!=0:
       total = total +num
print(total) # Note Formula sum of odd nums claude se liye 

#18 Take a number and print all of its factors.

num = int(input("Enter num: "))

for i in range (1,num+1):
    if num % i == 0:
        print(i) # Note Formula Factor claude se liye 
    

#19 Check whether a number is a Prime Number.
num = int(input("Enter Num: "))
is_prime = True
for i in range(2, num):
    if num % i == 0:
        is_prime = False
        break

if is_prime and num > 1:
    print("Prime")
else:
    print("Not Prime") # Note Prime No Formula Claude se liya hay

#20 Generate the first 10 Fibonacci numbers.
a,b = 0,1
for i in range(10):
    print(a)
    a,b = b,a+b # Note Formula + Code bi claude se liya hay likha mene hay kiuke ye mere liye phli bar tha 

#21 print numbers from 1 to 100. Skip every multiple of 4.
for i in range(1,101):
    if i %4==0:
     continue
    print(i) 

#22 Keep asking the user for a positive number.Stop only when they enter a positive number.

usernum = int(input("Enter Num: "))

i = 0
while usernum>0:
    print("Postive Num Enter Great")
    i = i+1
    print("S.No: ",i)
    usernum = int(input("Enter Num: "))   
else:
 print("you entering non-positive num")
    
print("Program Ended")

#23 print numbers from 1 to 50.
#Stop immediately when the square of a number becomes greater than 900.

for i in range(1,51):
    if i**2 >900:
        break
    print(i)

#24 print the following pattern:
'''1
22
333
4444
55555'''
# 24 Problem
for i in range(1,6):
    for j in range (i):
     print(i,end="")
    print()

#25 ⭐ Final Challenge – Mini Student Report Card
'''Take input:
Name
Roll Number
Marks in 5 subjects

Calculate:
Total
Average
Grade

Grade Rules:
90–100 → A+
80–89 → A
70–79 → B
60–69 → C
Below 60 → Fail

print a formatted report like:
========== REPORT CARD ==========
Name      : Muhammad Shanzail
Roll No   : 101
Total     : 438
Average   : 87.6
Grade     : A
Result    : PASS'''
#Problem 25

name = input("Enter Name: ")
rollnum = int(input("Enter Roll Num: "))    
mark1 = int(input("Enter Marks1 English: "))
mark2 = int(input("Enter Marks2 Maths: "))
mark3 = int(input("Enter Marks3 Physics: "))
mark4 = int(input("Enter Marks4 Chemistry: "))
mark5 = int(input("Enter Marks5 Biology: "))

total = sum([mark1,mark2,mark3,mark4,mark5])
average_total = total/5

if average_total>=90:
    Grade=("A+")
elif average_total>=80:
    Grade=("A")
elif average_total>=70:
    Grade=("B")
elif average_total>=60:
    Grade=("C")
else:
    Grade=("Fail")

if average_total>=60:
    result=("PASS")
else:
    result=("FAIL")

print("\n------------ReportCard---------")
print("Name:",name)
print("Rollnum:",rollnum)
print("Total:",total)
print("Average:",average_total)
print("Grade:",Grade)
print("Result:",result)

# TimeTaken = 125Mint 
# Note mene kuch jagah Formulas Claude se pouchen hay aur mention bi kiye hein comments se ke konse question me mene use kia hay kiuke me kitne formulas yad rakta isliye jiska nh aya claude se pouch liya but sara code likha mene hay 
# 🏆 100 Days Python Challenge – Day 6 Result (Corrected)
# Score: ⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐ (9.8/10)
# Overall Rating: 98/100 🏆 Python Master
