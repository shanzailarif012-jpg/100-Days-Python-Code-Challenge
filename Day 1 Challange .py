                        # 100 Days Python Challange 
                        # Day One(1) Python 25 Questions 
print("\t\t\t\t\tDev.Shanzail Backend Developer") # Name And Role

#1 Create a variable name and store your full name in it. Print it.

myname= ("Muhammad Shanzail")
print(myname)

#2 Create variables for your age, height, and whether you are a student or not. Print all values.

age = 21
height = 5.7
student= True

print("Age is:",age)
print("Height is:", height)
print(student)

#3 Check the data type of the value 25.5.

value = 25.5
print(type(value))

#4 Create two integer variables and print their sum.
no1 = 70
no2 = 30
print("Sum is",no1+no2)

#5 Convert the string "100" into an integer and add 50 to it.

num = ("100")
print(num)
num=int("100")
print(type(num))
print("50 is Add:",num+50)

#6 Create a string containing your favorite city and print it in uppercase

favcity = ("my favorite city is hyderabad")
print(favcity.upper())

#7 Print the length of the string "Python Programming".

language = ("Python Programming")
print(len(language))

#8 Extract the first character from the string "Computer"

character = ("Computer")
print(character[0])

#9 Extract the last character from the string "Developer".

lastcharacter = ("Developer")
print(lastcharacter[-1])

#10 Replace "World" with "Pakistan" in "Hello World".

letter = ("Hello World")
replace =letter.replace("World","Pakistan")
print(replace)

#11 Count how many times the letter "a" appears in "Banana" 

fruit = ("Banana")
print(fruit.count("a"))

#12 Take your first and last name as separate strings and combine them

firstname=("Muhammad")
lastname=(" Shanzail")
print(firstname+ lastname)

#13 Reverse the string "Python"

string=("Python")
print(string[::-1])

#14 Create a list of 5 favorite fruits and print it.

friuts = ["Apple","Banana","Strawberry","Mango","WaterMellon"]
print(friuts,(type(friuts))) # Letter List 

#15 Add "Orange" to the fruit list.

print(friuts.append("Orange"))
print("Orange is Added",friuts)

#16 Remove the second item from the list.

# friuts.remove("Banana") # First Method 
friuts.pop(1) # Second Method With Pop
print(friuts)

#17 Print the first and last element of a list

print("First Fruits:",friuts[0])
print("Last Fruits:",friuts[-1])

#18 Sort a list of numbers in ascending order

numlist = [32,76,88,35,23]
numlist.sort()
print("Assending Order:",numlist)

#19 Create a tuple containing 5 colors and print the third color

colors = ("White","Red","Black","Yellow","Green")
print("Third Color is:",colors[2])

#20 Find the length of a tuple.

'''print(len(colors))'''

#21 Create a dictionary containing your name, age, and city. Print it.

dict = {

    "Name":"Shanzail",
    "Age":21,
    "City":"Hyderabad"
}

print(dict)

#22 Access and print only the age from the dictionary

print("Age is",dict["Age"])

#23 Add a new key "profession" to the dictionary.

dict.update({"Profession":"Backend Developer"})
print(dict)

#24 Create a set containing numbers 1, 2, 3, 3, 4, 4, 5 and print it. What do you observe?

nums = {1,2,3,3,4,4,5}
print(nums,type(nums))

#25 Add the number 10 to a set and then remove 2 

nums.add(10)
print("10 is Added in Set",nums)
nums.remove(2)
print("2 is Removed",nums)


# Total Time Taken = 58 Mint
# 🏆 100 Days Python Challenge – Day 1 Result
# Score: ⭐⭐⭐⭐⭐⭐⭐⭐⭐☆ (9.5/10)
# Overall Rating: 95/100 🎉