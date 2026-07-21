                        #  100 Days Python Challange 
                        # Day Fiveteen(15) Python 25 Questions 
print("\t\t\t\t\tDev.Shanzail Backend Developer") # Name And Role

                            # Basics
#1 Create a class Student.

class Student:
    pass


#2 Create an object of Student.

class Student:
    pass

s1 = Student()


#3 Add attributes: name age Print both values.

class Student:
    pass

s1 = Student()
s1.name ="Dev_Shanzail"
s1.age = 21
print(s1.name , s1.age)


#4 Create a class Car with attributes:brand model Create an object and print them.

class Car:
    pass

car = Car()
car.brand = "Honda"
car.model = 2026
print(f"Car Brand {car.brand}")
print(f"Car Model {car.model}")


#5 Create a class Book with attributes: title author Print both.

class Book:
    pass

book = Book()
book.tittle = "Clean Code"
book.author = "Robert C. Martin"

print(f"Book Tittle is {book.tittle}")
print(f"Book Author is {book.author}")

                                            # Methods
'''#6 Create a class Person.
Add a method:
introduce()
Output:
Hello, my name is Ali'''

class Person:

    def introduce(self):
        print("Hello My name is Ali")

person = Person()
person.introduce()


'''#7 Create a class Dog.
Method:
bark()
Print:
Woof Woof'''

class Dog:

    def bark(self):
        print("Woof Woof")

dog = Dog()
dog.bark()

'''#8 Create a class Calculator.
Methods:
add()
subtract()'''

class Calculator:
    
    def add(self):
        pass

    def subtract():
        pass


# 9 Create a class Rectangle. Method area()

class Rectangle:

    def area(self):
        pass


'''#10 Create a class Circle.
Method:
area()
Use 3.14'''

class Circle:

    def area(self,radius):
        Area = 3.14 * radius * radius
        print(f"The Area of Cicle is {Area}")

checkcircle = Circle()
checkcircle.area(5)

                                        # Using self

'''#11 Create a class Student.
Method:
show()
Print name and age using self.'''

class Student:

    def show(self):
        name = "Ali"
        age = "21"
        print(f"Name is {name} , Age is {age}")

student = Student()
student.show()


'''#12 Create a class Employee.
Attributes:
name
salary

Method:
display()'''

class Employee:

    def display(self):
        print(f"Employe name is {self.name}")
        print(f"Employe salaray is {self.salaray}")

e1 = Employee()
e1.name = "Ahmed"
e1.salaray = 123000
e1.display()


'''#13 Create a class Mobile.
Attributes:
company
price

Method
details()'''

class Mobile:

    def details(self):
        print(f"Compnay {self.company}")
        print(f"Price {self.price}")

m = Mobile()
m.company = "Apple Iphone 17Pro Max"
m.price = 7800000
m.details()


                                    # Multiple Objects

#14 Create two Student objects. Print both.

class Student:
    
    def details(self):
        print(f"Name : {self.name}")
        print(f"Roll No : {self.rollno}\n")

s1 = Student()
s1.name = "Yahya"
s1.rollno = 1

s2 = Student()
s2.name = "Azlan"
s2.rollno = 2

s1.details()
s2.details()


#15 Create three Car objects. Print all

class Car:

    def details(self):
        print(f"CarName: {self.name}")
        print(f"Model: {self.model}")
        print(f"Price: {self.price}\n")

car1 = Car() # Object 1 
car1.name = "Honda City"
car1.model = 2026
car1.price = 5150000

car2 = Car() # Object 2 
car2.name = "Toyota Carolla Grande 1.8"
car2.model = 2026
car2.price = 8500000

car3 = Car() # Object 3 
car3.name = "Suzuki Alto"
car3.model = 2026
car3.price = 3200000

car1.details()
car2.details()
car3.details()


'''#16 Create a class Bank.
Attribute:
balance

Method:
show_balance()'''

class Bank:

    def show_balance(self):
        print(f"Your Balance is {self.balance}")

checkbalance = Bank()
checkbalance.balance = "120 PKR"
checkbalance.show_balance()


'''#17 Create a class Temperature.
Method:
is_hot()
Return True if temperature > 35.'''

class Temperature:

    def is_hot(self):
        if self.temperature > 35:
            return True
        else:
            return False
            

checktemperature = Temperature()
checktemperature.temperature = 34
print(checktemperature.is_hot())


#18 Create a class Number. Method: is_even()

class Number:

    def is_even(self):
        if self.number % 2 == 0:
            return True
        else:
            return False
        
checknum = Number()
checknum.number = 24
print(checknum.is_even())

#19 Create a class Marks. Method: result() Return Pass if marks ≥ 40.

class Marks:

     def result(self):
        if self.marks >= 40:
            return "PASS"
        else:
            return "FAIL"

checkmarks = Marks()
checkmarks.marks = 56
print(checkmarks.result())         


#20 Create a class Square. Method: square() Return square of a number.
class Sqaure:

    def sqaure(self):
        return (f"The Sqaure of Num is {self.num * self.num}")

numsqaure = Sqaure()
numsqaure.num = 3
print(numsqaure.sqaure())


#21 Create a class Counter. Method: increment() Increase value by 1.

class Counter:

    def increment(self):
        self.num = self.num + 1

count = Counter()
count.num = 1
count.increment()
print(count.num)

count.increment()
print(count.num)

count.increment()
print(count.num)


'''#22 Create a class Greeting.
Method:
say_hello()
Print a greeting message.'''

class Greeting:

    def say_hello(self):
        print("Good morning! Wishing you a wonderful day.")

check = Greeting()
check.say_hello()


'''#23 Create a class Player.
Attributes:
name
score

Method:
show_score()'''

class Player:

    def show_score(self):
        print(f"Player Name {self.name}")
        print(f"Player score {self.score}")

p1 = Player()
p1.name = "Messi"
p1.score = 76
p1.show_score()


'''#24 Create a class Movie.
Attributes:
name
rating

Method:
display()'''

class Movie:

    def display(self):
        print(f"Movie Name {self.moviename} Rating is :{self.rating}")

check = Movie()
check.moviename = "Dabang2"
check.rating ="10/8.5"
check.display()


#25⭐ Final Challenge (25)
'''Create a class: StudentReport
Store:
Name
Roll Number
Marks (5 subjects)

Create methods to:
Calculate Total
Calculate Average
Find Highest Marks
Find Lowest Marks
Calculate Grade
Result (Pass/Fail)

Print:
========== STUDENT REPORT ==========
Name:
Roll No:
Marks:
Total:
Average:
Highest:
Lowest:
Grade:
Result:
==================================='''
# Problem 25
class Studentreport:

    def calculate_total(self):
        total = 0
        for i in self.marks:
            total += i
        return total
    
    def calculate_average(self):
        total = self.calculate_total()
        average = total / len(self.marks)
        return average

    def highest_marks(self):
     highest = self.marks[0]

     for mark in self.marks:

        if mark > highest:
            highest = mark
     return highest

    def lowest_marks(self):
        lowest = self.marks[0]

        for mark in self.marks:
            
            if mark < lowest:
                lowest = mark
        return lowest

    def calculate_grade(self):
        average = self.calculate_average()
        if average >= 90:
            grade = "A+"
        elif average >= 80:
            grade = "A"
        elif average >= 70:
            grade = "B"
        elif average >= 60:
            grade = "C"
        elif average >= 50:
            grade = "D"
        else:
            grade = "F"
        return grade
#         
    def result(self):
        average = self.calculate_average()
        if average >= 40:
            result = "PASS"
        else:
            result = "FAIL"
        return result

    def display_report(self):

        print("========== STUDENT REPORT ==========")
        print(f"Name: {self.name}")
        print(f"Rollno: {self.rollno}")
        print(f"Marks: {self.marks}")
        print(f"Total: {self.calculate_total()}")
        print(f"Average: {self.calculate_average()}")
        print(f"Highest_Marks: {self.highest_marks()}")
        print(f"Lowest_Marks: {self.lowest_marks()}")
        print(f"Grade: {self.calculate_grade()}")
        print(f"Result: {self.result()}")
        print("===================================\n")

# Student 1 
student1 = Studentreport()
student1.name = "Shafique Ahmed"
student1.rollno = 1
student1.marks = [76,65,87,45,34]
student1.display_report()

# Student 2
student2 = Studentreport()
student2.name = "Jamil uddin"
student2.rollno = 2
student2.marks = [54,65,76,43,32]
student2.display_report()

# Student 3
student3 = Studentreport()
student3.name = "Ameen Memon"
student3.rollno = 3
student3.marks = [88,78,79,89,91]
student3.display_report()

# TimeTaken = 125MINT
# ⭐ Rating: 9.4/10
# Dev.Shanzail 🔥 Day 15 OOP Practice Review
# Sabse pehle: Great job. Tumne OOP ka first day kaafi achay se complete kiya. 
# Tumne classes, objects, attributes, methods aur self ko practically use kiya hai.

