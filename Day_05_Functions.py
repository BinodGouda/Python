"""
Functions in Python

1. Introduction:
   - A function is a block of code that performs a specific task
   - Functions help in code reusability and organization
   - Defined using the 'def' keyword

2. Types of Functions:
   - Built-in Functions
   - User-defined Functions
   - Anonymous Functions (Lambda Functions)
   - Recursive Functions
"""

# Built-in Functions
print("1. Built-in Functions:")
# Examples: print(), len(), type(), int(), str(), etc.
print("Example of built-in function 'len':", len("Hello"))

# User-defined Functions
print("\n2. User-defined Functions:")

# Example 1: Simple function
def greet():
    print("Hello, welcome to Python functions!")

greet()

# Example 2: Function with parameters
def add(a, b):
    return a + b

result = add(5, 3)
print("Sum of 5 and 3 is:", result)

# Example 3: Function with default parameters
def greet_user(name="Guest"):
    print(f"Hello, {name}!")

greet_user("Alice")
greet_user()

# Example 4: Function with return value
def square(x):
    return x * x

print("Square of 4 is:", square(4))

# Anonymous Functions (Lambda Functions)
print("\n3. Anonymous Functions (Lambda Functions):")

# Example 1: Simple lambda function
square = lambda x: x * x
print("Square of 6 using lambda is:", square(6))

# Example 2: Lambda function with multiple arguments
add = lambda a, b: a + b
print("Sum of 7 and 2 using lambda is:", add(7, 2))

# Example 3: Using lambda with built-in functions
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x * x, numbers))
print("Squared numbers using lambda and map:", squared_numbers)

# Recursive Functions
print("\n4. Recursive Functions:")

# Example: Factorial using recursion
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print("Factorial of 5 is:", factorial(5))

"""
Key Points to Remember:
1. Functions help in breaking down complex problems into smaller, manageable parts
2. Built-in functions are provided by Python and can be used directly
3. User-defined functions are created by the user to perform specific tasks
4. Lambda functions are small anonymous functions defined using the lambda keyword
5. Recursive functions call themselves to solve problems that can be broken down into smaller, repetitive tasks
6. Use functions to improve code readability, reusability, and maintainability
"""
