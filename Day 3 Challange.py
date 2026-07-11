                            # 100 Days Python Challange 
                        # Day Three(3) Python 25 Questions 
print("\t\t\t\t\tDev.Shanzail Backend Developer") # Name And Role

#1 Take a number from the user and check whether it is positive or negative

user_num = int(input("Enter Num: "))

if user_num>=0:
    print("Positive Number")
else:
    print("Negative Number")

#2 Check whether a number is even or odd. 

checknum = int(input("Enter Num: "))

if checknum %2==0:
    print("Even")
else:
    print("Odd")

#3 Take the user's age and check if they are eligible to vote (18 or above)

age = int(input("Enter Yours Age: "))

if age>=18:
    print("Eligible For Vote")
elif age<0:
    print("Invalid Num ")
else:
    print("Not Eligible For Voting")

#4 Take two numbers and print the greater number.

check_greater1 = int(input("Enter Num1: "))
check_greater2= int(input("Enter Num2: "))

if check_greater1 > check_greater2:
    print("Num 1 is greater ")
else:
    print("Num 2 is greater")

#5 Take three numbers and print the largest one.

num1 = int(input("Enter Num 1: "))
num2 = int(input("Enter Num 2: "))
num3 = int(input("Enter Num 3: "))

if num1>num2 and num1>num3:
    print("number 1 is largest num",num1)
elif num2>num1 and num2>num3:
    print("number 2 is largest num",num2)
elif num3>num1 and num3>num2:
    print("number 3 is largest num",num3)

#6 Check whether two numbers are equal. 

a = int(input("Enter Num1: "))
b = int(input("Enter Num2: "))

print(a==b)

#7 check whether one number is greater than or equal to another.

a1 = int(input("Enter Num1: "))
a2 = int(input("Enter Num2: "))
print(a1>=a2)

#8 Take a password from the user. If it is "python123", print Access Granted, otherwise print Access Denied.

user_password = "python123"

password=input("Enter Password: ")

if password==user_password:
    print("Access Granted")
else:
    print("Access Denied")

#9 Check whether a number is divisible by 5.

division_num = int(input("Enter Num: "))

if division_num%5==0:
    print("'Yes' Divisible By 5")
else:
    print("'No' Not Divisible By 5")

#10 Check whether a number is divisible by both 3 and 5.

checknum_Divisible = int(input("Enter Num: "))

if checknum_Divisible%3==0 and checknum_Divisible%5==0:
    print("Yes Divisile by Both")
else:
    print("No")

#11 Take age and check if the person is eligible for a driving license (Age ≥ 18).

user_age = int(input("Enter Age: "))

if user_age>=18:
    print("Eligible For Driving license Test")
else:
    print("No Sorry Not Eligible For Driving license")

#12 ake username and password. If both are correct, print Login Successful. Username: admin Password: 12345

Username= "admin"
Password= "12345"

checkusername = input("Enter Username: ")
checkpassword = input("Enter password: ")

if checkusername==Username and checkpassword==Password:
    print("Login SuccessFul")
else:
    print("Falied Login Try Again")

#13 Take a number and check whether it lies between 1 and 100.

numbercheck = int(input("Enter Num: "))

if 1<= numbercheck<=100:
    print("yes Between 1 to 100")
else:
    print("Not lies Between 1 to 100")

#14 Check whether a year entered by the user is a leap year.

year = int(input("Enter year: "))

if year %4==0 and year%100!=0 or year %400==0:
    print("This is Leap Year")
else:
    print("This year is not Leap Year")

#15 Take a character and check whether it is a vowel or a consonant.

character = input("Enter Character: ")

vowels = ("a,e,i,o,u")

if character in vowels:
    print("This is Vowel")
else:
    print("This is Consonant")

#16 Take marks from the user and print:
'''90–100 → A+
80–89 → A
70–79 → B
60–69 → C
Below 60 → Fail'''
# Problem
marks = int(input("Enter Your Marks: "))

if marks>90<100:
    print("A+")
elif marks>80<89:
    print("A")
elif marks>70<79:
    print("B")
elif marks>60<69:
    print("C")
else:
    print("Fail")

#17 Take the user's salary.
'''Salary > 100000 → High Income
50000–100000 → Medium Income
Below 50000 → Low Income'''

#Problem 

salary = int(input("Enter Salary: "))

if salary>100000:
    print("High Income")
elif 50000 <= salary <= 100000:
    print("Medium Income")
else:
    print("Low Income")

#18 Take a temperature value.
'''Above 35 → Hot
20–35 → Normal
Below 20 → Cold'''
#Problem
temp = int(input("Enter Temperature: "))

if temp>35:
    print("Hot")
elif temp >20<=35:
    print("Normal")
else:
    print("Cold")

#19 Take a number and check:
'''Positive Even
Positive Odd
Negative Even
Negative Odd
Zero'''
# Problem
numcheck = int(input("Enter Num: "))

if numcheck==0:
    print("Zero")
elif numcheck>0 and numcheck %2==0:
    print("Postive Even")
elif numcheck>0 and numcheck %2!=0:
    print("Postive Odd")
elif numcheck<0 and numcheck %2==0:
    print("Negative Even")
else:
    print("Negative Odd")

#20 Take two numbers and an operator (+, -, *, /) from the user and perform the calculation using if-elif.

num1 = int(input("Enter Num1: "))
operator = input("Enter Operator: ")
num2 = int(input("Enter Num2: "))

if  operator=="+":
    print(num1+num2)
elif  operator=="-":
    print(num1-num2)
elif  operator=="*":
    print(num1*num2)
elif  operator=="%":
    print(num1%num2)
else:
    print("Invalid Operator")

#21 Check whether a person can enter a movie.Condition:Age must be 18 or above.

userage = int(input("Enter Age: "))

if userage>=18:
    print("Enter to Movie")
else:
    print("Sorry Opps Not Enter")

#22 Take a number and check whether it is a multiple of 7.

multiple_num = int(input("Enter Num: "))

if multiple_num%7==0:
    print("Yes")
else:
    print("No")

#23 Take a student's attendance percentage.
'''75% or above → Allowed in Exam
Below 75% → Not Allowed'''
# Problem
attendence = int(input("Enter Attendence: "))

if attendence >=75:
    print("Allowed in Exam")
else:
    print("Not Allowed in Exam")

#24 Take the user's gender (M or F) and print a greeting.
'''Example:
M → Welcome Sir
F → Welcome Ma'am'''
# Problem
gender = input("Enter Gender: ")

if gender=="M":
    print("Welcome Sir")
elif gender=="F":
    print("Welcome Maam")
else:
    print("Only M and F Letter is Allowed")

#25 ⭐ Challenge – Student Result System
'''Take input:    
Name
Roll Number
Marks (out of 100)

Print:
Name
Roll Number
Marks
Grade
Pass/Fail

Grading:
90–100 → A+
80–89 → A
70–79 → B
60–69 → C
Below 60 → Fail'''

name = input("Enter Name: ")
rollnum = int(input("Enter Roll Num: "))
marks = int(input("Enter Marks 100 out of: "))

#Conditions 
if marks>90<100:
    Grade=("A+")
elif marks>80<89:
    Grade=("A")
elif marks>70<79:
    Grade=("B")
elif marks>60<69:
    Grade=("C")
else:
    Grade=("Fail")

# Final Output
print("\n\t\t\t Result")
print("Name:",name)
print("rollnum:",rollnum)
print("marks:",marks)
print("Grade",Grade)


# TimeTaken = 97Mint
# 🏆 100 Days Python Challenge – Day 3 Result
# Score: ⭐⭐⭐⭐⭐⭐⭐⭐☆☆ (8.8/10)
# Overall Rating: 88/100 🥉 Bronze