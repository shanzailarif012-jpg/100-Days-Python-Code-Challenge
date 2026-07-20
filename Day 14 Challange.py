                         #  100 Days Python Challange 
                        # Day Fourteen(14) Python 25 Questions 
print("\t\t\t\t\tDev.Shanzail Backend Developer") # Name And Role

#1 Create a file named intro.txt and write: Hello Python

with open("Day14_01_intro.txt" , "w") as f:
    intro = f.write("My Name is Dev Shanzail")

#2 Read the contents of intro.txt.

with open("Day14_01_intro.txt" , "r") as f:
    f.read()


#3 Append the line: Welcome to File Handling to the same file.

with open ("Day14_01_intro.txt" , "a" ) as f:
    f.write("\nWelcome to File Handling")


#4 Read the updated file.

with open("Day14_01_intro.txt" , "r") as f:
   f.read()


#5 Write your name, age, and country to profile.txt

with open ("Day14_02_myprofile.txt" , "w") as f:
    f.write("Name : Dev_Shanzail\nAge: 21\nCity: Pakistan")

#6 Read profile.txt and print each line separately.

with open("Day14_02_myprofile.txt" , "r") as f:
    line1=f.readline()
    line2=f.readline()
    line3=f.readline()
    print(line1, end="")
    print(line2, end="")
    print(line3, end="")


#7 Count the total number of characters in a file.

with open ("Day14_01_intro.txt" )as f:
    character = f.read()
    print(len(character)) # Method 1 With length
    count = 0
    for i in character:
        count += 1
    print(count) # Method 2 With loop


#8 Count the total number of words in a file.

with open ("Day14_01_intro.txt" ) as f:
    words = f.read()

    list_words = words.split()

    total_words = 0
    for i in list_words:
         total_words += 1
    print(total_words) 


#9 Count the total number of lines.

with open("Day14_02_myprofile.txt") as f:
    lines = f.readlines()

    count = 0
    for i in lines:
     count += 1
    print(count)


#10 Create a function: read_file(filename) that prints the file contents.

def read_file(filename):
    
    with open ("Day14_02_myprofile.txt") as f:
        read = f.read()
        print(read)


read_file("filename")


#11 Create a function: write_file(filename, text) Write the given text to the file.

def write_file(filename , text ):

    with open ("Day14_03_mainfile.txt" , "w") as f:
        text = f.write("Hello Everyone")

write_file("filename" , "text")


#12 Create a function: append_file(filename, text) Append text.

def append_file(filename , text):
    with open ("Day14_03_mainfile.txt" , "a") as f:
        text = f.write("\nWelcome Backkkkk")

append_file("filename" , "text")


#13 Check whether the word Python exists in a file. Return True or False.
def word():

    with open ("Day14_04_checkexists.txt" ) as f:
     text = f.read()
    word = "Python"
    if word in text:
        return True
    else:
        return False

check_exists = word()
print(check_exists)

#14 Count how many times Python appears in a file.

with open("Day14_04_checkexists.txt") as f:
    read = f.read()

    print(read.count("Python"))

#15 Replace every occurrence of Python with Java

with open ("Day14_04_checkexists.txt") as f:
    text = f.read()

    replace_word = text.replace("Python" , "Java")

with open ("Day14_04_checkexists.txt" ,"w") as f:
    f.write(replace_word)


#16 Remove every occurrence of Java from the file.

with open ("Day14_04_checkexists.txt") as f:
    content = f.read()

remove_java = content.replace("Java" , "")

with open ("Day14_04_checkexists.txt" , "w") as f:
    f.write(remove_java) 


#17 Copy the contents of one file into another. Example: myprofile.txt to backup.txt

with open ("Day14_02_myprofile.txt") as f:
    text = f.read()

with open ("Day14_05_backup.txt" , "w") as f:
    f.write(text)


#18 Merge two files into one. Example: file1.txt and file2.txt  = merged.txt

with open ("Day14_01_intro.txt") as f:
    text1 = f.read()

with open ("Day14_02_myprofile.txt") as f:
    text2 = f.read()

merged = text1+ "\n" +text2 


with open("Day14_06_merged.txt","w") as f:
    f.write(merged)


#19 Read a file and print only lines containing Python

with open ("Day14_03_mainfile.txt") as f:
    lines = f.readlines()
    for line in lines :
        if "Python" in line:
            print(line)


#20 Print the line numbers where Python appears.

with open ("Day14_03_mainfile.txt") as f:
    text = f.readlines()

    lineno = 1
    for line in text:
        if "Python" in line:
            print (lineno)
        lineno +=1 


#21 Count uppercase letters in a file.

with open ("Day14_03_mainfile.txt") as f:
    text = f.read()

    letter = 0
    for word in text:
        if word.isupper():
            letter +=1

    print(letter)


#22 Count lowercase letters in a file.

with open("Day14_03_mainfile.txt") as f:
    text = f.read()

    letter = 0
    for word in text:
        if word.islower():
            letter += 1
    print(letter)
    

#23 Count digits in a file.

with open ("Day14_03_mainfile.txt") as f:
    text = f.read()

    count = 0
    for num in text:
        if num.isdigit():
            count += 1
    print(count)


#24 Count spaces in a file.

with open ("Day14_01_intro.txt") as f:
    text = f.read()

    count = 0
    for space in text:
        if space==" ":
            count+=1
    print(count)


# ⭐ Final Challenge
'''25.Create a function: file_report(filename)
Return:
Total Characters
Total Words
Total Lines
Uppercase Letters
Lowercase Letters
Digits
Spaces
Number of times "Python" appears

Print:
========== FILE REPORT ==========
File Name :
Characters :
Words :
Lines :
Uppercase :
Lowercase :
Digits :
Spaces :
Python Count :
================================='''

# Problem 25

def file_report(filename):

    with open (filename) as f:
        text = f.read()

        characters = 0
        words = 0
        lines = 0
        uppercase = 0
        lowwercase = 0
        digits = 0
        spaces = 0
        python_count = 0
        # Character Loop
        for character in text:
            characters +=1

            if character.isupper():
                uppercase +=1

            if character.islower():
                lowwercase +=1 
            
            if character.isdigit():
                digits +=1
            
            if character == " ":
                spaces += 1

        # Word Loop
        word_List = text.split()
        words = 0
        for word in word_List:
                words +=1

                if word == "Python":
                    python_count +=1 
        # Lines Loop   

        with open(filename) as f:
            all_lines = f.readlines()

        lines = 0
        for line in all_lines:
         lines += 1
    
    return characters , words , lines , uppercase , lowwercase , digits , spaces , python_count

characters, words, lines, uppercase, lowercase, digits, spaces, python_count = file_report("Day14_02_myprofile.txt")

print("========== FILE REPORT ==========")
print("Characters :", characters)
print("Words :", words)
print("Lines :", lines)
print("Uppercase :", uppercase)
print("Lowercase :", lowercase)
print("Digits :", digits)
print("Spaces :", spaces)
print("Python Count :", python_count)
print("=================================")


# # TimeTaken = 85MINT
# Day 14 Rating: 9.6/10 ⭐⭐⭐⭐⭐
# What you did well
# ✅ Used with open() correctly throughout.
# ✅ Practiced all major modes: r, w, a.
# ✅ Worked with read(), readline(), and readlines().
# ✅ Counted characters, words, lines, digits, uppercase, lowercase, and spaces manually.
# ✅ Solved copy, merge, replace, remove, and search problems.
# ✅ Completed the final challenge on your own.



 
