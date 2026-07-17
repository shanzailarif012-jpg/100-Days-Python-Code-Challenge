                         #  100 Days Python Challange 
                        # Day Eleven(11) Python 25 Questions 
print("\t\t\t\t\tDev.Shanzail Backend Developer") # Name And Role

#1 Create a function count_vowels(text) that returns the number of vowels
vowels = "aeiouAEIOU"
def count_vowels(text):
    count = 0
    for i in text:
        if i in vowels:
          count+=1
    return count
text = input("Enter text here: ")
check = count_vowels(text)
print(check)

#2 Create a function count_consonants(text) that returns the number of consonants. 
vowels = "aeiouAEIOU"
def count_consonants(text):
    count = 0
    for i in text:
        if i.isalpha() and i not in vowels:
         count+=1
    return count
text = input("Enter Text here: ")
check = count_consonants(text)
print(check)

#3 Create a function count_digits(text) that returns how many digits are in the string.

def count_digits(text):
    count = 0
    for i in text:
        if i.isdigit():
            count+=1
    return count
text = input("Enter Text Num: ")
check = count_digits(text)
print(check)

#4 Create a function count_spaces(text) that returns the number of spaces.

def count_spaces(text):
    count = 0
    for i in text:
        if i==" ":
         count+=1 
    return count

text = input("Enter Text Here: ")
check = count_spaces(text)
print(check)

#5 Create a function reverse_words(sentence) that returns every word reversed but keeps the word order.
'''Example: "I love Python"
Output:
"I evol nohtyP"'''
#Problem 5
def reversed_words(sentence):
    words = sentence.split()
    reversed_words_list = []
    for word in words:
        reverse = word[::-1]
        reversed_words_list.append(reverse)
    return" ".join(reversed_words_list)
    
        
sentence = input("Enter Sentense: ")
check = reversed_words(sentence)
print(check)

#6 Create a function list_sum(numbers) without using sum()
l1 = [1,5,5,4]
def list_sum(l1):
    total = 0
    for num in l1:
        total += num
    return total
check = list_sum(l1)
print(check)

#7 Create a function list_product(numbers) that returns the product of all numbers.
l1 = [1,5,5,4]
def product_list(l1):
    product = 1
    for num in l1:
        product *= num
    return product

check = product_list(l1)
print(check)

#8 Create a function largest(numbers) without using max()

def largest(num):
    largest = num[0]

    for i in num:
     if i > largest:
        largest = i
    return largest
num = [10,80,20]
check = largest(num)
print(check)

#9 Create a function smallest(numbers) without using min()

def smallest(num):
    samllest = num[0]
    for i in num:
        if i < samllest:
            samllest = i

    return samllest

num = [20,90,70,15]
check=smallest(num)
print(check)

#10 Create a function count_positive(numbers)

def count_positive(num):
    count = 0
    for i in num:
        if i > 0:
         count = count + 1
    return count
    
num = [70,-15,-20,15,20]
check = count_positive(num)
print(f"In this list there are {check} positive numbers")

#11 Create a function count_negative(numbers).
def count_negative(num):
    count = 0
    for i in num:
        if i < 0:
            count = count + 1
    return count

num = [23,87,-76,7,-3,-6,87]
check = count_negative(num)
print(f"In this list there are {check} negative numbers")

#12 Create a function count_zero(numbers)

def zero(num):
    count =  0
    for i in num:
        if i ==0:
            count = count + 1
    return count
num = [34,56,75,0,23,-87,0]
check = zero(num)
print(f"In this list there are {check} Zeros(0)")

#13 Create a function square_list(numbers) that returns a new list containing squares
l1 = [ 2 , 4 , 5]
def sqaure_list(l1):
    l2 = []
    for i in l1:
      sqaure_num= i**2
      l2.append(sqaure_num)
    return(l2)

check = sqaure_list(l1)
print(f"The Square of list 1{l1} Square After is {check}")

#14 Create a function cube_list(numbers) that returns a new list containing cubes.
l1 = [ 2 , 3 , 5]

def cube(l1):
    l2 = []
    for num in l1:
        cube_num = num*num*num
        l2.append(cube_num)
    return(l2)

check = cube(l1)
print(f"The Cube of list {l1} after Cube is {check}")

#15 Create a function even_numbers(numbers) that returns only even numbers as a list

l1 = [2,3,4,5,6,7,8]
def even_num(l1):
    l2 = []
    for i in l1:
        if i %2==0:
         l2.append(i)
    return(l2)
check = even_num(l1)
print(f"The List of Even Numbers is {check}")

#16 Create a function odd_numbers(numbers) that returns only odd number
l1 = [2,3,4,5,6,7,8]
def odd_num(l1):
    l2 = []
    for i in l1:
        if i %2 != 0:
          l2.append(i)
    return(l2)
check = odd_num(l1)
print(f"The List of odd numbers is {check}")

#17 Create a function is_palindrome(text) that returns True or False

def is_palindrome(text):
    reverse = text[::-1]
    if text == reverse:
        return True
    else:
        return False
text = input("Enter Text: ")
Check = is_palindrome(text)
print(f"The Text Enter {text} is {Check}")

#18 Create a function count_letter(text, letter) that returns how many times a letter appears.
def count_letter(text,letter):
    count = 0
    # letter1 = letter
    for letter1 in text:
        if letter1 == letter:
         count +=1
    return count
        
text = input("Enter Text: ")
letter = input("Which Letter Count You Find Enter: ")

check = count_letter(text,letter)
print(check)

#19 Create a function remove_spaces(text) that returns the string without spaces

def remove_spaces(text):
    character = ""
    for i in text:
        if i != " ":
            character += i
    return character
     

text = input("Enter Text: ")
check = remove_spaces(text)

#20 Create a function capitalize_words(sentence) that returns every word with the first letter capitalized.

def capitalize_word(sentence):
    new_word_list = []
    word = sentence.split()
    for words in word:
     new_word =words.capitalize()
     new_word_list.append(new_word)
    return " ".join(new_word_list)

sentence = input("Enter Sentence: ")
check = capitalize_word(sentence)
print(check)

#21 Create a function second_smallest(numbers)
num = [15, 10, 2, 8]
def second_smallest(num):
    smallest_num = num[0]
    second_smallest_num = num[1]
    for numbers in num:
        if numbers < smallest_num:
            second_smallest_num = smallest_num
            smallest_num = numbers
        elif numbers > smallest_num and numbers < second_smallest_num:
            second_smallest_num = numbers
    return second_smallest_num

check = second_smallest(num)
print(f"Second Smallest Num is {check}")

#22 Create a function second_largest(numbers) without sorting
num = [15, 10, 12, 8]
def second_largest(num):
    largest_num = num[0]
    sec_largest_num = num[1]

    for numbers in num:
        if numbers > largest_num:
            sec_largest_num = largest_num
            largest_num = numbers
        elif numbers < largest_num and numbers > sec_largest_num:
            sec_largest_num = numbers
    return sec_largest_num

check = second_largest(num)
print(f"Second Largest Num is: {check}")

#23 Create a function unique_elements(numbers) that returns a list without duplicate values
num = [13,10,9,10,20,9]
def unique_elements(num):
    new_unique_numbers = []
    for numbers in num:
        if numbers not in new_unique_numbers:
            new_unique_numbers.append(numbers)
    return new_unique_numbers

check = unique_elements(num)
print(f"The List of Unique Numbers is {check}")

#24 Create a function merge_lists(list1, list2) that returns a single merged list
list1 = [10,20,30,40]
list2 = [40,50,60]

def merge_lists(list1,list2):
    list3_merge = list1 + list2
    return list3_merge

check = merge_lists(list1,list2)
print(f"Merge of List1 {list1} and list2 {list2}\n is after Merge is {check}")


#25 ⭐ Final Challenge – Library Book Report
'''Create a function: library_report(student_name, books)
Where books is a list of book names.

The function should return:
Student Name
Total Books
Longest Book Name
Shortest Book Name
Books in Alphabetical Order
First Book
Last Book

Print the output like:
========== LIBRARY REPORT ==========
Student Name :
Total Books  :
Longest Book :
Shortest Book:
First Book   :
Last Book    :
Books        :
===================================='''
def libaray_report(student_name,books):
    totalbooks = len(books)

    longestbooks = books[0]

    shortestbooks = books[0]

    for book in books:
        if len(book) > len(longestbooks):
            longestbooks = book
        if len(book) < len(shortestbooks):
            shortestbooks = book

    alphabatical_book = sorted(books)
    first_book = books[0]
    last_book = books[-1]

    return(student_name,totalbooks,longestbooks,shortestbooks,first_book,last_book,alphabatical_book)



books = []

for i in range(5):
    book = input(f"Enter Book {i+1} Name: ")
    books.append(book)

student_name = input("Enter Student Name: ")

(
    student_name,
    total_books,
    longest_book,
    shortest_book,
    first_book,
    last_book,
    alphabetical_books) =libaray_report(student_name, books)

print("\n========== LIBRARY REPORT ==========")
print("Student Name : ", student_name)
print("Total Books  : ", total_books)
print("Longest Book : ", longest_book)
print("Shortest Book: ", shortest_book)
print("First Book   : ", first_book)
print("Last Book    : ", last_book)
print("Books        : ", alphabetical_books)
print("===================================")

#TimeTaken = 95Mint
#  Day 11 Rating : ⭐ Overall Rating: 9.7/10 (Excellent)







            

        