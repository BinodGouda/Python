# Day_02_TypeCasting.py

"""
Getting User Input for Different Data Types
1. String: Directly use input(), as it returns a string.
   user_string = input("Enter a string: ")

2. Integer: Use int() to convert the input string to an integer.
   user_int = int(input("Enter an integer: "))

3. Float: Use float() to convert the input string to a float.
   user_float = float(input("Enter a float: "))

4. List: You can split a string input into a list.
   user_list = input("Enter a list of items separated by spaces: ").split()

5.Tuple: Convert a list to a tuple.
   user_tuple = tuple(user_list)

6. Set: Convert a list to a set to remove duplicates.
   user_set = set(user_list)

7. Dictionary: You can prompt for key-value pairs and convert them into a dictionary.
   user_dict = dict(input("Enter key-value pairs separated by commas (key:value): ").split(","))
"""


# This script demonstrates type casting in Python

# Implicit Type Casting
print("Implicit Type Casting:")
int_num = 5
float_num = 2.5
result = int_num + float_num  # int_num is implicitly converted to float
print(f"{int_num} + {float_num} = {result}")

# Explicit Type Casting
print("\nExplicit Type Casting:")
float_num = 2.5
int_num = int(float_num)  # float_num is explicitly converted to int
print(f"Converting {float_num} to int gives {int_num}")

# Converting string to int
str_num = "10"
int_num = int(str_num)  # string is explicitly converted to int
print(f"Converting '{str_num}' to int gives {int_num}")

# Converting int to string
int_num = 20
str_num = str(int_num)  # int is explicitly converted to string
print(f"Converting {int_num} to string gives '{str_num}'")

# Converting float to string
float_num = 3.14
str_num = str(float_num)  # float is explicitly converted to string
print(f"Converting {float_num} to string gives '{str_num}'")

# Converting string to float
str_num = "3.14"
float_num = float(str_num)  # string is explicitly converted to float
print(f"Converting '{str_num}' to float gives {float_num}")

# Type Casting Functions in Python
print("\nType Casting Functions in Python:")
print("1. int(): Converts a value to an integer.")
print("2. float(): Converts a value to a float.")
print("3. str(): Converts a value to a string.")
print("4. ord(): Converts a character to its Unicode code point (integer).")
print("5. chr(): Converts an integer (Unicode code point) back to a character.")
print("6. hex(): Converts an integer to a hexadecimal string.")
print("7. oct(): Converts an integer to an octal string.")
print("8. tuple(): Converts an iterable to a tuple.")
print("9. set(): Converts an iterable to a set (removing duplicates).")
print("10. list(): Converts an iterable to a list.")
print("11. dict(): Converts a sequence of key-value pairs to a dictionary.")

# Getting User Input for Different Data Types
print("\nGetting User Input for Different Data Types:")
user_string = input("Enter a string: ")
print(f"You entered the string: {user_string}")

user_int = int(input("Enter an integer: "))
print(f"You entered the integer: {user_int}")

user_float = float(input("Enter a float: "))
print(f"You entered the float: {user_float}")

user_list = input("Enter a list of items separated by spaces: ").split()
print(f"You entered the list: {user_list}")

user_tuple = tuple(user_list)
print(f"You converted the list to a tuple: {user_tuple}")

user_set = set(user_list)
print(f"You converted the list to a set: {user_set}")

user_dict = dict(item.split(":") for item in input("Enter key-value pairs separated by commas (key:value): ").split(","))
print(f"You entered the dictionary: {user_dict}")