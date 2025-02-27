"""
In Python, numbers are a fundamental data type used to represent numeric values. Python supports several types of numbers, which can be categorized as follows:

1. Integer (int):
Integers are whole numbers, which can be positive, negative, or zero.
They do not have a fractional part.
Example: -5, 0, 42.


2. Floating Point (float):
Floats are numbers that contain a decimal point or are in exponential (scientific) notation.
They can represent real numbers and can be positive or negative.
Example: 3.14, -0.001, 2.5e3 (which is equivalent to 2500.0).


3. Complex Numbers (complex):
Complex numbers consist of a real part and an imaginary part, represented as a + bj, where a is the real part and b is the imaginary part.
Example: 3 + 4j, -1 - 2j
"""

# Day 01: Numbers in Python

# Integer
integer_var1 = 10
integer_var2 = -5
integer_var3 = 0

# Floating Point
float_var1 = 3.14
float_var2 = -0.001
float_var3 = 2.5e3  # Equivalent to 2500.0

# Complex Numbers
complex_var1 = 3 + 4j
complex_var2 = -1 - 2j

# Outputting Numbers and Their Types
print("Integer Variables:")
print(integer_var1, type(integer_var1))  # Output: 10 <class 'int'>
print(integer_var2, type(integer_var2))  # Output: -5 <class 'int'>
print(integer_var3, type(integer_var3))  # Output: 0 <class 'int'>

print("\nFloating Point Variables:")
print(float_var1, type(float_var1))  # Output: 3.14 <class 'float'>
print(float_var2, type(float_var2))  # Output: -0.001 <class 'float'>
print(float_var3, type(float_var3))  # Output: 2500.0 <class 'float'>

print("\nComplex Variables:")
print(complex_var1, type(complex_var1))  # Output: (3+4j) <class 'complex'>
print(complex_var2, type(complex_var2))  # Output: (-1-2j) <class 'complex'>