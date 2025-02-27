'''
Variable Names:
Variable names in Python can consist of letters (both uppercase and lowercase), digits, and underscores. However, they cannot start with a digit.
Variable names are case-sensitive, meaning myVar and myvar are considered different variables.
It's recommended to use descriptive names that convey the purpose of the variable, such as age, total_price, or 
'''

# Day 01: Variables and Data Types in Python

# Variable Names
# Variable names can contain letters, digits, and underscores, but cannot start with a digit.
my_variable = 10
myVariable = 20
MyVariable = 30

# Assigning Multiple Values
a, b, c = 1, 2, 3
x = y = z = 0

# Outputting Variables
name = "Alice"
print(name)  # Output: Alice


'''
Global Variables:
A global variable is a variable that is defined outside of any function and can be accessed throughout the entire program.
If you create a variable with the same name inside a function, this variable will be local, and can only be used inside the function. The global variable with the same name will remain as it was, global and with the original value.
To modify a global variable inside a function, you need to use the global keyword. For example
'''

count = 0  # Global variable

def increment():
    global count
    count += 1

'''
Data Types:
Python has several built-in data types, including:
Integers: Whole numbers, e.g., 5, -3.
Floats: Decimal numbers, e.g., 3.14, -0.001.
Strings: Text data, e.g., "Hello, World!".
Booleans: Represents True or False.
Lists: Ordered collections of items, e.g., [1, 2, 3].
Tuples: Immutable ordered collections, e.g., (1, 2, 3).
Dictionaries: Key-value pairs, e.g., {"name": "Alice", "age": 25}.
'''

# Data Types

'''
Built-in Data Types
In programming, data type is an important concept.

Variables can store data of different types, and different types can do different things.

Python has the following data types built-in by default, in these categories:

Text Type:	str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview
None Type:	NoneType
'''

'''
Setting the Data Type
Example	                                        Data Type	
x = "Hello World"	                            str	
x = 20	                                        int	
x = 20.5	                                    float	
x = 1j	                                        complex	
x = ["apple", "banana", "cherry"]	            list	
x = ("apple", "banana", "cherry")	            tuple	
x = range(6)	                                range	
x = {"name" : "John", "age" : 36}	            dict	
x = {"apple", "banana", "cherry"}	            set	
x = frozenset({"apple", "banana", "cherry"})	frozenset	
x = True	                                    bool	
x = b"Hello"	                                bytes	
x = bytearray(5)	                            bytearray	
x = memoryview(bytes(5))	                    memoryview	
x = None	                                    NoneType
'''
'''
Setting the Data Type
Example	                                        Data Type	
x = str("Hello World")	                        str	
x = int(20)	                                    int	
x = float(20.5)	                                float	
x = complex(1j)	                                complex	
x = list(("apple", "banana", "cherry"))	        list	
x = tuple(("apple", "banana", "cherry"))	    tuple	
x = range(6)	                                range	
x = dict(name="John", age=36)	                dict	
x = set(("apple", "banana", "cherry"))	        set	
x = frozenset(("apple", "banana", "cherry"))	frozenset	
x = bool(5)	                                    bool	
x = bytes(5)	                                bytes	
x = bytearray(5)	                            bytearray	
x = memoryview(bytes(5))                        memoryview
'''


# Integers
integer_var = 5

# Floats
float_var = 3.14

# Strings
string_var = "Hello, World!"

# Booleans
bool_var = True

# Lists
list_var = [1, 2, 3]

# Tuples
tuple_var = (1, 2, 3)

# Dictionaries
dict_var = {"name": "Alice", "age": 25}

# Outputting Data Types
print(type(integer_var))  # Output: <class 'int'>
print(type(float_var))    # Output: <class 'float'>
print(type(string_var))   # Output: <class 'str'>
print(type(bool_var))     # Output: <class 'bool'>
print(type(list_var))     # Output: <class 'list'>
print(type(tuple_var))    # Output: <class 'tuple'>
print(type(dict_var))     # Output: <class 'dict'>