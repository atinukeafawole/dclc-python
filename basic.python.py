Exercise 1

def check_product_or_sum(num1: int, num2: int) -> int:
    product = num1 * num2
    if product <= 1000:
        return product
    return num1 + num2



Exercise 2
print("Printing current and previous number sum in a range(10)")
previous_num = 0

for i in range(10):
    x_sum = previous_num + i
    print(f"Current Number {i} Previous Number {previous_num} Sum: {x_sum}")



Exercise 3
 word = "pynative"
print("Original String is ", word)

even_chars = word[0::2]

print("Printing only even index chars")
for char in even_chars:
    print(char)   



Exercise 4
def remove_chars(word, n):
    print('Original string:', word)
    res = word[n:]
    return res

print("Removing characters from a string")
print(remove_chars("pynative", 4))
print(remove_chars("pynative", 2))




Exercise 5
a = 5
b = 10
print(f"Before Swap: a = {a}, b = {b}")

a, b = b, a

print(f"After Swap: a = {a}, b = {b}")

