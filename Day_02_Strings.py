"""
Python Strings Tutorial
===================
This module covers everything you need to know about strings in Python.
"""

# 1. String Basics
# Strings in Python are surrounded by either single or double quotation marks
print("\n1. Basic String Creation:")
str1 = 'Hello using single quotes'
str2 = "Hello using double quotes"
print(str1)
print(str2)

# 2. Quotes Inside Strings
print("\n2. Using Quotes Inside Strings:")
print("It's alright")  # Using single quote inside double quotes
print('He said "Python is awesome!"')  # Using double quotes inside single quotes
print('It\'s also possible with escape character')  # Using escape character

# 3. String Assignment
print("\n3. String Assignment to Variables:")
message = "Python is fun"
print(message)

# 4. Multiline Strings
print("\n4. Multiline Strings:")
multiline_string = """This is a multiline string.
It can span across multiple lines
without using escape characters.
Pretty cool, right?"""
print(multiline_string)

# 5. String Length
print("\n5. String Length:")
text = "Hello, World!"
print(f"Length of '{text}' is: {len(text)}")

# 6. String Indexing and Slicing
print("\n6. String Indexing and Slicing:")
print("=" * 40)
sample_text = "Python Programming"
print(f"Original text: '{sample_text}'")

# 6.1 Basic Indexing
print("\n6.1 Basic Indexing:")
print(f"First character (index 0): '{sample_text[0]}'")      # Returns 'P'
print(f"Third character (index 2): '{sample_text[2]}'")      # Returns 't'
print(f"Last character (index -1): '{sample_text[-1]}'")     # Returns 'g'
print(f"Second to last (index -2): '{sample_text[-2]}'")     # Returns 'n'

# 6.2 String Slicing [start:end:step]
print("\n6.2 String Slicing:")
# Basic slicing
print(f"Characters from index 2 to 8: '{sample_text[2:8]}'")     # Returns 'thon P'
print(f"Characters from start to 6: '{sample_text[:6]}'")        # Returns 'Python'
print(f"Characters from 7 to end: '{sample_text[7:]}'")          # Returns 'Programming'

# 6.3 Advanced Slicing with Step
print("\n6.3 Advanced Slicing with Step:")
print(f"Every second character: '{sample_text[::2]}'")           # Takes every 2nd character
print(f"Every third character: '{sample_text[::3]}'")            # Takes every 3rd character
print(f"Reverse the string: '{sample_text[::-1]}'")             # Reverses the string

# 6.4 Slicing with Negative Indices
print("\n6.4 Slicing with Negative Indices:")
print(f"Last 5 characters: '{sample_text[-5:]}'")               # Returns last 5 characters
print(f"Everything except last 5: '{sample_text[:-5]}'")        # Excludes last 5 characters
print(f"From 5th last to 2nd last: '{sample_text[-5:-2]}'")    # Returns characters between

# Visual representation of positive and negative indices
print("\nVisual Index Representation:")
print("String:  P  y  t  h  o  n     P  r  o  g  r  a  m  m  i  n  g")
print("Pos idx: 0  1  2  3  4  5  6  7  8  9  10 11 12 13 14 15 16")
print("Neg idx:-17-16-15-14-13-12-11-10-9 -8 -7 -6 -5 -4 -3 -2 -1")

# 7. String Methods
print("\n7. String Methods:")
print("=" * 50)

# 7.1 Case Manipulation Methods
print("\n7.1 Case Manipulation Methods:")
text = "Python Programming"
print(f"Original text: '{text}'")
print(f"Upper case: '{text.upper()}'")          # Converts to uppercase
print(f"Lower case: '{text.lower()}'")          # Converts to lowercase
print(f"Title case: '{text.title()}'")          # Capitalizes first letter of each word
print(f"Capitalize: '{text.capitalize()}'")      # Capitalizes first letter of string
print(f"Swapcase: '{text.swapcase()}'")         # Swaps case of each character

# 7.2 Whitespace Handling Methods
print("\n7.2 Whitespace Handling Methods:")
text_with_space = "   Python   "
print(f"Original text: '{text_with_space}'")
print(f"Left strip: '{text_with_space.lstrip()}'")    # Removes leading whitespace
print(f"Right strip: '{text_with_space.rstrip()}'")   # Removes trailing whitespace
print(f"Strip all: '{text_with_space.strip()}'")      # Removes both leading and trailing whitespace

# 7.3 Search and Replace Methods
print("\n7.3 Search and Replace Methods:")
search_text = "Python is amazing, Python is fun"
print(f"Original text: '{search_text}'")
print(f"Count 'Python': {search_text.count('Python')}")          # Counts occurrences
print(f"Find 'is': {search_text.find('is')}")                    # Returns first occurrence index
print(f"Right find 'is': {search_text.rfind('is')}")            # Returns last occurrence index
print(f"Replace first: '{search_text.replace('Python', 'Java', 1)}'")  # Replace with count
print(f"Replace all: '{search_text.replace('Python', 'Java')}'")       # Replace all occurrences

# 7.4 String Testing Methods
print("\n7.4 String Testing Methods:")
print(f"Is 'ABC123' alphanumeric? {'ABC123'.isalnum()}")        # Tests if alphanumeric
print(f"Is 'ABC' alphabetic? {'ABC'.isalpha()}")                # Tests if alphabetic
print(f"Is '123' numeric? {'123'.isnumeric()}")                 # Tests if numeric
print(f"Is '  ' whitespace? {'  '.isspace()}")                  # Tests if whitespace
print(f"Is 'Title' title case? {'Title'.istitle()}")            # Tests if titlecased
print(f"Is 'UPPER' uppercase? {'UPPER'.isupper()}")             # Tests if uppercase
print(f"Is 'lower' lowercase? {'lower'.islower()}")             # Tests if lowercase

# 7.5 String Splitting and Joining
print("\n7.5 String Splitting and Joining:")
# Splitting
sentence = "Python,Java,C++,JavaScript"
words = sentence.split(',')
print(f"Original text: '{sentence}'")
print(f"Split into list: {words}")
print(f"Split with maxsplit=2: {sentence.split(',', 2)}")

# Joining
join_list = ['Python', 'Java', 'C++']
print(f"Original list: {join_list}")
print(f"Joined with comma: '{','.join(join_list)}'")
print(f"Joined with space: '{' '.join(join_list)}'")

# 7.6 String Padding and Alignment
print("\n7.6 String Padding and Alignment:")
text = "Python"
width = 20
print(f"Left aligned: '{text.ljust(width, '-')}'")    # Left justify
print(f"Right aligned: '{text.rjust(width, '-')}'")   # Right justify
print(f"Centered: '{text.center(width, '-')}'")       # Center
print(f"Zero-filled: '{text.zfill(width)}'")          # Pad with zeros

# 7.7 String Checking and Formatting
print("\n7.7 String Checking and Formatting:")
text = "This is a sample text with some numbers 12345"
print(f"Starts with 'This': {text.startswith('This')}")         # Check prefix
print(f"Ends with '45': {text.endswith('45')}")                 # Check suffix
print(f"Partition at 'sample': {text.partition('sample')}")      # Partition string
print(f"Remove prefix 'This': '{text.removeprefix('This')}'")   # Remove prefix
print(f"Remove suffix '45': '{text.removesuffix('45')}'")       # Remove suffix

# 7.8 String Encoding and Decoding
print("\n7.8 String Encoding and Decoding:")
text = "Hello, 世界"
print(f"Original text: '{text}'")
print(f"UTF-8 encoded: {text.encode('utf-8')}")
print(f"ASCII encoded (with replace): {text.encode('ascii', 'replace')}")

# 8. String Concatenation
print("\n8. String Concatenation:")
first = "Hello"
second = "World"
print(f"Using + operator: {first + ' ' + second}")
print(f"Using join method: {' '.join([first, second])}")

# 9. String Formatting
print("\n9. String Formatting:")
name = "Alice"
age = 25
# Using format() method
print("My name is {} and I'm {} years old".format(name, age))
# Using f-strings (Python 3.6+)
print(f"My name is {name} and I'm {age} years old")

# 10. String Check Methods
print("\n10. String Check Methods:")
text = "Python123"
print(f"Is 'Python123' alphanumeric? {text.isalnum()}")
print(f"Is 'Python123' alphabetic? {text.isalpha()}")
print(f"Is '123' numeric? {'123'.isnumeric()}")

# 11. Escape Characters
print("\n11. Escape Characters:")
print("Line 1\nLine 2")  # New line
print("Tab\tExample")    # Tab
print("This will print a backslash: \\")  # Backslash

# 12. String Immutability
print("\n12. String Immutability:")
name = "Python"
print("Strings are immutable. You can't change individual characters.")
print("Instead, create a new string:")
new_name = name.replace('P', 'J')
print(f"Original: {name}")
print(f"New: {new_name}")
