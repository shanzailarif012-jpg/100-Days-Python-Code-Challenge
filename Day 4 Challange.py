                            # 100 Days Python Challange 
                        # Day Four(4) Python 25 Questions 
print("\t\t\t\t\tDev.Shanzail Backend Developer") # Name And Role

#1 Print numbers from 1 to 10 using a for loop.

n = int(input("Enter Num: "))
for i in range(1,11):
    print(i)

#2 Print numbers from 10 to 1 in reverse order.

for i in range(10,0,-1):
    print(i)

#3 Print all even numbers from 1 to 20.

for i in range(0,21):
    if i % 2 == 0:
        print(i)

#4 Print all odd numbers from 1 to 20.

for i in range(1,21):
    if i % 2!=0:
     print(i)

#5 Print the multiplication table of 5. 

for i in range(1,11):
    print(f"{5} * {i} = {5 * i}")

#6 Print numbers from 1 to 10 using a while loop.

i = 1
while (i<11):
    print(i)
    i = i+1 

#7 Print numbers from 10 to 1 using a while loop.

i = 10

while i>0:
    print(i)
    i = i-1

#8 Calculate the sum of numbers from 1 to 100 using a while loop.
sum = 0
i = 1 

while i <=100:
    sum = sum + i
    i = i +1
print(sum)

#9 Print the multiplication table of any number entered by the user using a while loop.

n = int(input("Enter Num: "))
i = 1

while i <11:
    print(f"{n} * {i} = {n * i}")
    i = i +1 

#10 Keep asking the user to enter a password until they enter "python123"

correctpassword = "python123"

userpass = input("Enter Password: ")

while correctpassword!= userpass:
    print("try again")
    userpass = input("Enter Password: ")
print("Login Success")
    
#11 Print numbers from 50 to 100 using range()

for i in range(50,101):
    print(i)

#12 Print numbers from 100 to 0 with a step of 10.

for i in range(100,0,-10):
    print(i)

#13 Print the square of numbers from 1 to 10.

for i in range(1,11):
    print(i**2)

#14 Print the cube of numbers from 1 to 10. 

for i in range(1,11):
    print(i*i*i)

#15 Print all numbers divisible by 3 between 1 and 50.

for i in range(1,51):
    if i % 3==0:
        print(i)

#16 Print numbers from 1 to 20, but stop when the number becomes 15.
# using While Loop
i = 1 
while i<21:
      if i ==15:
          print("found No 15")
          break
      print(i)
      i = i +1


# using For Loop
for i in range (1,21):
   print(i)
   if i == 15:
      print("Found",i)
      break
   
#17 Print numbers from 1 to 20, but skip 10.

for i in range(1,21):
    if i==10:
        print("No 10 Is Skip")
        continue
    print(i)

#18 Print numbers from 1 to 30, skipping all multiples of 5.

for i in range(1,31):
    if i %5==0:
        continue
    print(i)

#19 Keep taking user input until the user enters 0.

user = 0

num = int(input("Enter Num: "))

while num!= user:
    print("Enter Again")
    num = int(input("Enter Num: "))
   
print("Yes Corrct you entring num 0")

#20 Create a simple ATM PIN checker.Correct PIN: 1234 note Keep asking until the correct PIN is entered.

pin = 1234

user = int(input("Enter Your Pin: "))

while pin!= user:
    print("Wrong Pin Enter Again")
    user = int(input("Enter Pin: "))

print("Login Success")

#21 Print the following pattern:
'''*
**
***
****
*****'''
# Problem
n = int(input("Enter Num: "))


for i in range(1,n+1):
    print("*"*i,end="")
    print()

#22 Print the following pattern:
'''*****
****
***
**
*'''
# Problem
n = int(input("Enter Num: "))

for i in range(n,0,-1):
    print("*" * i , end="")
    print()

#23 Print a 5 × 5 square using *.
'''*****
*****
*****
*****
*****'''
# Problem 23 Mene isko advance kardiya hay user se input leke 
n = int(input("Enter :"))
for i in range (1,n+1):
    print("*" * n,end="")
    print()

#24 Print the multiplication tables from 2 to 5 using nested loops.

for table in range(2,6):
    for i in range(1,11):
        print(f"{table} * {i} = {table * i}")
    print()

#25 ⭐ Challenge – Number Guessing Game
'''Store a secret number (for example, 7).
Ask the user to guess it.
Keep asking until the correct number is entered.
If the guess is wrong, print:
Too High (if guess is greater)
Too Low (if guess is smaller)
When guessed correctly, print:
Congratulations! You guessed the correct number.'''
# Problem 25 
num = 7

usernum = int(input("Enter Num: "))
while num!= usernum:
    print("Wrong")
    if num<usernum:
        print("too high")
    else:
        print("too Smaller")
    usernum = int(input("Enter Num: "))
print("Congratulations! You guessed the correct number.")

# Time Taken = 74Mint
# 🏆 100 Days Python Challenge – Day 4 Result
# Score: ⭐⭐⭐⭐⭐⭐⭐⭐⭐☆ (9.7/10)
# Overall Rating: 97/100 🥇 Gold
# ✅ Excellent Work!