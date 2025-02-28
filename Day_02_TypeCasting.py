# Day_02_TypeCasting.py

"""
Type casting is the process of converting a variable from one data type to another. This is often necessary in programming to ensure that operations are performed correctly, especially when dealing with different types of data.
There are two main types of type casting:
Implicit Type Casting (Automatic Type Conversion):
This occurs when the compiler automatically converts one data type to another without explicit instruction from the programmer.
For example, when an integer is added to a float, the integer is automatically converted to a float.

   int_num = 5
   float_num = 2.5
   result = int_num + float_num  # int_num is implicitly converted to float



Explicit Type Casting (Type Conversion):
This requires the programmer to specify the type conversion. This is done using built-in functions like int(), float(), str(), etc.
For example, converting a float to an integer:

   float_num = 2.5
   int_num = int(float_num)  # float_num is explicitly converted to int

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

# Converting character to Unicode code point
char = 'A'
unicode_value = ord(char)  # character is converted to its Unicode code point
print(f"Converting '{char}' to Unicode code point gives {unicode_value}")

# Converting Unicode code point to character
unicode_value = 65
char_value = chr(unicode_value)  # Unicode code point is converted back to character
print(f"Converting {unicode_value} to character gives '{char_value}'")

# Converting integer to hexadecimal string
int_num = 255
hex_value = hex(int_num)  # integer is converted to hexadecimal string
print(f"Converting {int_num} to hexadecimal gives {hex_value}")

# Converting integer to octal string
int_num = 8
oct_value = oct(int_num)  # integer is converted to octal string
print(f"Converting {int_num} to octal gives {oct_value}")

# Converting list to tuple
list_data = [1, 2, 3]
tuple_value = tuple(list_data)  # list is converted to tuple
print(f"Converting {list_data} to tuple gives {tuple_value}")

# Converting list to set
list_data = [1, 2, 2, 3]
set_value = set(list_data)  # list is converted to set (removing duplicates)
print(f"Converting {list_data} to set gives {set_value}")

# Converting iterable to list
iterable_data = (1, 2, 3)
list_value = list(iterable_data)  # iterable is converted to list
print(f"Converting {iterable_data} to list gives {list_value}")

# Converting key-value pairs to dictionary
key_value_pairs = [(1, 'a'), (2, 'b')]
dict_value = dict(key_value_pairs)  # key-value pairs are converted to dictionary
print(f"Converting {key_value_pairs} to dictionary gives {dict_value}")

