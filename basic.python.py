Exercise 1
Write a Python function that accepts two integer numbers. If the product of the two numbers is less than or equal to 1000, return their product; otherwise, return their sum.

def check_product_or_sum(num1: int, num2: int) -> int:
    product = num1 * num2
    if product <= 1000:
        return product
    return num1 + num2



Exercise 2
Iterate through the first 10 numbers (0–9). In each iteration, print the current number, the previous number, and their sum.

print("Printing current and previous number sum in a range(10)")
previous_num = 0

for i in range(10):
    x_sum = previous_num + i
    print(f"Current Number {i} Previous Number {previous_num} Sum: {x_sum}")



Exercise 3
Display only those characters which are present at an even index number in given string.

 word = "pynative"
print("Original String is ", word)

even_chars = word[0::2]

print("Printing only even index chars")
for char in even_chars:
    print(char)   



Exercise 4
Write a function to remove characters from a string starting from index 0 up to n and return a new string.

def remove_chars(word, n):
    print('Original string:', word)
    res = word[n:]
    return res

print("Removing characters from a string")
print(remove_chars("pynative", 4))
print(remove_chars("pynative", 2))




Exercise 5
Write a program to swap the values of two variables, a and b, without using a third temporary variable.

a = 5
b = 10
print(f"Before Swap: a = {a}, b = {b}")

a, b = b, a

print(f"After Swap: a = {a}, b = {b}")



Exercise 6 
Write a program that calculates the factorial of a given number (e.g., 5!) using a for loop.

num = 5
factorial = 1

for i in range(1, num + 1):
    factorial = factorial * i

print(f"The factorial of {num} is {factorial}")



Exercise 7
Create a list of 5 fruits. Add a new fruit to the end of the list, then remove the second fruit (at index 1).

fruits = ["apple", "banana", "cherry", "date", "elderberry"]

fruits.append("fig")

fruits.pop(1)

print(fruits)




Exercise 8
Write a program that takes a string and reverses it (e.g., “Python” becomes “nohtyP”).

text = "Python"

reversed_text = text[::-1]

print(f"Original: {text}")
print(f"Reversed: {reversed_text}")




Exercise 9
Write a program to count the total number of vowels (a, e, i, o, u) present in a given sentence.

sentence = "Learning Python is fun!"
vowels = "aeiou"
count = 0

for char in sentence.lower():
    if char in vowels:
        count += 1

print(f"Number of vowels: {count}")



Exercise 10
Given a list of integers, find and print both the largest and the smallest numbers.

nums = [45, 2, 89, 12, 7]

largest = max(nums)
smallest = min(nums)

print(f"Largest: {largest}")
print(f"Smallest: {smallest}")




Exercise 11
Write a script that takes a list containing duplicate items and returns a new list with only unique elements.


data = [1, 2, 2, 3, 4, 4, 4, 5]

unique_data = list(set(data))

print(f"Unique List: {unique_data}")





Exersise 12
Write a function to return True if the first and last number of a given list is the same. If the numbers are different, return False.

def first_last_same(number_list):
    print("Given list:", number_list)
    
    first_num = number_list[0]
    last_num = number_list[-1]
    
    if first_num == last_num:
        return True
    else:
        return False

numbers_x = [10, 20, 30, 40, 10]
print("result is", first_last_same(numbers_x))

numbers_y = [75, 65, 35, 75, 30]
print("result is", first_last_same(numbers_y))




Exercise 13
Iterate through a given list of numbers and print only those numbers which are divisible by 5.

num_list = [10, 21, 35, 46, 50]
print("Given list is", num_list)
print("Divisible by 5:")

for num in num_list:

    if num % 5 == 0:
        print(num)




Exercise 14
Write a program to find how many times the substring “Emma” appears in a given string.

str_x = "Emma is good developer. Emma is a writer"
count = str_x.count("Emma")
print(f"Emma appeared {count} times")




Exercise 15
Print the following pattern where each row contains a number repeated a specific number of times based on its value.

for num in range(1, 6):
    for i in range(num):
        print(num, end=" ") # end=" " keeps it on the same line
    print("\n")
