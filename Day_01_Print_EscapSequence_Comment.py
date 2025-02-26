# Day_01_Print_EscapSequence_Comment.py

# This program demonstrates the use of comments, escape sequences, and print statements in Python.

# Comments in Python
# Comments are used to explain the code and make it more readable. They are ignored by the Python interpreter.
# There are two types of comments in Python:
# 1. Single-line comments: Start with a hash (#) and continue to the end of the line.
# 2. Multi-line comments: Enclosed in triple quotes (""" or ''') and can span multiple lines.

# Single-line comment example
print("Hello, World!")  # This prints a greeting

# Multi-line comment example
"""
This program will show:
1. How to use escape sequences
2. How to format print statements
"""
'''
This program will show:
1. How to use escape sequences
2. How to format print statements
'''

# Escape Sequences in Python
# Escape sequences are special characters that allow you to include characters in a string that would otherwise be difficult to type.
# They start with a backslash (\) followed by a character. Some common escape sequences include:
# - \n: New line
# - \t: Tab
# - \\: Backslash
# - \': Single quote
# - \": Double quote

# Using escape sequences
print("Hello,\nWorld!")  # Prints "Hello," and "World!" on a new line
print("Tab\tSpace")      # Prints "Tab" followed by a tab space and then "Space"
print("Backslash: \\")   # Prints "Backslash: \"

# Using formatted print statements
# Formatted print statements allow you to embed expressions inside string literals, using curly braces {}.
# This is useful for including variable values in strings.

name = "Alice"
age = 30
print(f"{name} is {age} years old.")  # Outputs: Alice is 30 years old.

# Additional examples of escape sequences
print("This is a single quote: \'")  # Prints: This is a single quote: '
print("This is a double quote: \"")   # Prints: This is a double quote: "
print("This is a backslash: \\")      # Prints: This is a backslash: \
