                        #  100 Days Python Challange 
                        # Day Sixteen(16) Python 25 Questions 
print("\t\t\t\t\tDev.Shanzail Backend Developer") # Name And Role

'''#1Create a class Student.
Constructor should store:
name
age
Create an object and print both values.'''

class Student:

    def __init__(self,name,age):
        self.name = name
        self.age = age

s1 = Student("Dev_Shanzail" , 21)
print(s1.name)
print(s1.age)


'''#2Create a class Car.
Constructor:
brand
model
Method:
display()'''

class Car:

    def __init__(self,brand,model):
        self.brand = brand
        self.model = model

    def display(self):
        print(self.brand)
        print(self.model)

c1 = Car("Honda" , 2026)
c1.display()


'''#3 Create a class Book
Constructor:
title
author
Method:
details()'''

class Book:

    def __init__(self,title,author):
        self.title = title
        self.author = author

    def details(self):
        print(f"The Book Title is: {self.title}")
        print(f"The Book Author is: {self.author}")

b1 = Book("Python Course" , "Dev_Shanzail")
b1.details()


'''#4 Create a class Mobile
Constructor:
company
price
Method:
show()'''

class Mobile:

    def __init__(self,company,price):
        self.company = company
        self.price = price

    def show(self):
        print(f"The Mobile Company is: {self.company}")
        print(f"The Mobile price is: {self.price}")

m1 = Mobile("Apple", 120000)
m1.show()


'''#5 Create a class Person
Constructor:
name
Method:
introduce()
Output:
Hello, my name is Ali'''

class Person:

    def __init__(self,name):
        self.name = name

    def introduce(self):
        print(f"Hello, my name is {self.name}")

p1 = Person("Ali")
p1.introduce()


'''#6 Create a class Rectangle
Constructor:
length
width
Method:
area()'''

class Rectangle:

    def __init__(self,length,width):
        self.length = length
        self.width = width

    def area(self):
        area = self.length * self.width
        print(f"The Area of Rectangle is {area}")

a1 = Rectangle(25,20)
a1.area()


'''#7 Create a class Circle
Constructor:
radius
Method:
area()
Use 3.14'''

class Circle:

    def __init__(self,radius):
        self.radius = radius

    def area(self):
        area = 3.14 * self.radius**2
        print(f"The Area of Circle is: {area}")

c1 = Circle(35)
c1.area()


'''#8 Create a class Square
Constructor:
side
Method:
area()'''

class Square:

    def __init__(self,side):
        self.side = side
    
    def area(self):
        area = self.side ** 2
        print(f"The Area of Sqaure is {area}")

s1 = Square(25)
s1.area()


'''#9 Create a class Bank
Constructor:
balance
Method:
show_balance()'''

class Bank:

    def __init__(self,balance):
        self.balance = balance   

    def show_balance(self):
        print(f"The Current Balance is {self.balance}")

c1 = Bank(10000)
c1.show_balance()


'''#10 Create a class Temperature
Constructor:
temperature
Method:
is_hot()
Return True if temperature > 35.'''

class Temperature:

    def __init__(self,temperature):
        self.temperature = temperature

    def is_hot(self):
        if self.temperature > 35:
            return True
        else:
            return False
        
t1 = Temperature(56)
print(t1.is_hot())


'''#11 Create a class Employee
Constructor:
name
salary
Method:
display()'''

class Employee:

    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

    def display(self):
        print(f"Employee Name: {self.name}")
        print(f"Employee salary: {self.salary}")

e1 = Employee("Tahir Habib" , 15000)
e1.display()


'''#12 Create a class Player
Constructor:
name
score
Method:
show_score()'''

class Player:

    def __init__(self,name,score):
        self.name = name
        self.score = score

    def show_score(self):
        print(f"Player Name: {self.name}")        
        print(f"Player score: {self.score}")  

p1 = Player("Baber Azam" , 96)
p1.show_score()   



'''#13Create a class Movie
Constructor:
name
rating
Method:
display()'''

class Movie:

    def __init__(self,name,rating):
        self.name = name
        self.rate = rating

    def display(self):
        print(f"Movie Name: {self.name}")
        print(f"Movie rating: {self.rate}")

m1 = Movie("Lucky Basker" , "10/8")
m1.display()


'''#14 Create a class Counter
Constructor:
value = 0
Method:
increment()
Increase value by 1.'''

class Counter:

    def __init__(self,value = 0):
        self.value = value

    def increment(self):
        self.value += 1

c1 = Counter()
c1.increment()
c1.increment()
c1.increment()
print(c1.value)


'''#15 Create a class Calculator
Constructor:
a
b
Methods:
add()
subtract()
multiply()
divide()'''

class Calculator:

    def __init__(self,a,b):
        self.a = a
        self.b = b

    def add(self):
        print(f"The Addition of {self.a} and {self.b} is {self.a + self.b}")

    def subtarct(self):
        print(f"The Subtarction of {self.a} and {self.b} is {self.a - self.b}")

    def multiply(self):
        print(f"The Multiplication of {self.a} and {self.b} is {self.a * self.b}")

    def divide(self):
        print(f"The Division of {self.a} and {self.b} is {self.a // self.b}")

n1 = Calculator(20,5)
n1.add()
n1.subtarct()
n1.multiply()
n1.divide()


'''#16 Create a class BankAccount
Constructor:
account_holder
balance
Methods:
deposit(amount)
show_balance()'''

class BankAccount:

    def __init__(self,account_holder,balance):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self,amount):
        self.amount = amount
    
    def show_balance(self):
        total_amount = self.balance + self.amount
        print(f"The Total Amount After Deposit is {total_amount}")

p1 = BankAccount("Dev_Shanzail",5000)
p1.deposit(5000)
p1.show_balance()



'''#17 Create a class StudentMarks
Constructor:
marks (list)
Methods:
total()
average()'''

class StudentMarks:

    def __init__(self,marks):
        self.marks = marks

    def total(self):
        totalmarks = sum(self.marks)
        return totalmarks

    def average(self):
        average = (self.total() / len(self.marks))
        print (average)

s1 = StudentMarks([20,20,30])
print(s1.total())
s1.average()


'''#18 Create a class Laptop
Constructor:
company
ram
storage
Method:
specs()'''

class Laptop:

    def __init__(self,company,ram,stoarge):
        self.company = company
        self.ram = ram
        self.storage = stoarge

    def specs(self):
        print(f"Company Name: {self.company}")
        print(f"Ram: {self.ram}")
        print(f"Storage: {self.storage}")
        print()

l1 = Laptop("Hp" , "8Gb" , "256SSD")
l1.specs()


'''#19 Create a class Dog
Constructor:
name
breed
Method:
bark()
Output:
Tom says Woof Woof'''

class Dog:

    def __init__(self,name,breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print("Tom Says Woof Woof")

d1 = Dog("Tom","German")
d1.bark()



'''#20 Create a class Number
Constructor:
number
Methods:
is_even()
square()'''

class Number:

    def __init__(self,number):
        self.number = number

    def is_even(self):
        if self.number % 2 == 0:
            print(f"The Num {self.number} is Even Number")
        else:
            print(f"The Num {self.number} is Not Even Number")
    
    def sqaure(self):
        print(f"The Sqaure of Num {self.number} is {self.number * self.number}")

n1 = Number(13)
n1.is_even()
n1.sqaure()



'''#21 Create a class Product
Constructor:
name
price
quantity
Methods:
total_price()
display()'''

class Product:

    def __init__(self,name,price,quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    
    def total_price(self):
        print(f"The Product {self.name} Total Price is {self.price}")

    
    def display(self):
        print(f"Product Name: {self.name}")
        # print(f"Product Price: {self.price}")
        print(f"Product Quantity: {self.quantity}")

p1 = Product("Hp Laptop" , 98000 , 100)
p1.display()
p1.total_price()



'''#22 Create a class LibraryBook
Constructor:
title
author
pages
Method:
details()'''

class LibraryBook:

    def __init__(self,title,author,pages):
        self.title = title
        self.author = author
        self.pages = pages

    def details(self):
        print(f"The Tittle of Book: {self.title}")
        print(f"The author of Book: {self.author}")
        print(f"The pages of Book: {self.pages}")

b1 = LibraryBook("Ultimate Python", "Robrt Robin Son", 101)
b1.details()



'''#23 Create a class Exam
Constructor:
student_name
marks (5 subjects)
Methods:
total()
average()
highest()'''


class Exam:

    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

    
    def total(self):
        return sum(self.marks)
        # print(f"The Total Sum of Marks is {total}")
        # return total

    def average(self):
        return self.total() / len(self.marks)
        # print (f"The Average is {average}")

    def highest(self):
        highest = self.marks[0]
        for mark in self.marks:
            if mark > highest:
             highest = mark
        return highest
        # print(f"The Highest Marks is {highest}")

result = Exam("Ebraheem",[88,85,54,59,76])
print(f"Total of Marks is {result.total()}")
print(f"Average of Marks is {result.average()}")
print(f"Highest of Marks is {result.highest()}")


'''#24 Create a class BankAccount
Constructor:
name
balance
Methods:
deposit()
withdraw()
show_balance()
Withdrawal should happen only if balance is sufficient.'''
        
class BankAccount:

    def __init__(self,name,balance):
        self.name = name
        self.balance = balance

    def deposit(self,deposit_am):
        self.deposit_am = deposit_am
        self.balance =self.balance + self.deposit_am
        print(self.balance)

    def withdraw(self,withdraw_am):
        self.withdraw_am = withdraw_am
        if self.balance >= self.withdraw_am:
            self.balance = self.balance - self.withdraw_am
            print(self.balance)
        else:
            print("Insufficient Balance,OOPs Not Enough Balance")
            

    def show_balance(self):
        print(f"Total Balance in Account is {self.balance} ")

p1 = BankAccount("Rohan",5000)
p1.deposit(0)
p1.withdraw(5001)
p1.show_balance()



#25 Final Challenge (25)
'''Create a class:
StudentManagement

Constructor
Store:
Student Name
Roll Number
Marks (5 subjects)

Methods
calculate_total()
calculate_average()
highest_marks()
lowest_marks()
calculate_grade()
result()

display_report()
Grade
90+  → A+
80+  → A
70+  → B
60+  → C
50+  → D
Below → F

Result
Average >= 40 → PASS
Otherwise → FAIL
Output Format
========== STUDENT REPORT ==========
Name            :
Roll Number     :
Marks           :
Total           :
Average         :
Highest Marks   :
Lowest Marks    :
Grade           :
Result          :
==================================='''

#Problem 25

class StudentManagement:

    def __init__(self,name,rollno,marks):
        self.name = name
        self.rollno = rollno
        self.marks = marks


    def calculate_total(self):
        total = sum(self.marks)
        return total
    

    def calculate_average(self):
        average = self.calculate_total() / len(self.marks)
        return average
    

    def highest_marks(self):
        highest = max(self.marks)
        return highest
    

    def lowest_marks(self):
        lowest = min(self.marks)
        return lowest
    

    def calculate_garde(self):
        average = self.calculate_average()
        if average >=90:
            garde = "A+"
        elif average >=80:
            garde = "A"
        elif average >=70:
            garde = "B"
        elif average >=60:
            garde = "C"
        elif average >=50:
            garde = "D"
        else:
            garde = "F"
        return garde
    

    def result(self):
        average = self.calculate_average()
        if average >=40:
            result = "PASS"
        else:
            result = "FAIL"

        return result

    def display_report(self):
        print("========== STUDENT REPORT ==========")
        print(f"Name : {self.name}")
        print(f"RollNo: {self.rollno}")
        print(f"Marks : {self.marks}")
        print(f"Total : {self.calculate_total()}")
        print(f"Average : {self.calculate_average()}")
        print(f"Highest Marks : {self.highest_marks()}")
        print(f"Lowest Marks : {self.lowest_marks()}")
        print(f"Grade : {self.calculate_garde()}")
        print(f"Result : {self.result()}")
        print("===================================")
        print()

s1 = StudentManagement("Usman",1,[27,76,98,65,60])
s1.display_report()

# TimeTaken = 135 
# 📊 Day 16 Review
# Overall Rating: 9.4/10 ⭐⭐⭐⭐⭐
# Difficulty: ⭐⭐⭐☆☆ (Intermediate)

        

        

    
        
        
        

        
        


        

