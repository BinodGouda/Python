"""
Python For Loop Tutorial
----------------------
For loops in Python are used to iterate over sequences (lists, tuples, strings, etc.)
or other iterable objects. They provide a simple and efficient way to repeat a set of
instructions for each item in a collection.
"""

# Basic For Loop with a List
def basic_list_loop():
    print("\n1. Basic List Loop:")
    fruits = ["apple", "banana", "cherry"]
    for fruit in fruits:
        print(f"Current fruit: {fruit}")

# For Loop with Range
def range_loop():
    print("\n2. Range Loop:")
    # range(start, stop, step)
    print("Counting from 0 to 4:")
    for i in range(5):  # 0 to 4
        print(f"Number: {i}")
    
    print("\nCounting from 2 to 8 with step 2:")
    for i in range(2, 9, 2):  # 2, 4, 6, 8
        print(f"Number: {i}")

# For Loop with Enumerate
def enumerate_loop():
    print("\n3. Enumerate Loop:")
    colors = ["red", "green", "blue"]
    for index, color in enumerate(colors):
        print(f"Index {index}: {color}")
    
    # Enumerate with start index
    print("\nEnumerate starting from 1:")
    for index, color in enumerate(colors, start=1):
        print(f"Index {index}: {color}")

# For Loop with Dictionary
def dictionary_loop():
    print("\n4. Dictionary Loop:")
    person = {
        "name": "John",
        "age": 30,
        "city": "New York"
    }
    
    # Iterating over keys
    print("Keys only:")
    for key in person:
        print(key)
    
    # Iterating over key-value pairs
    print("\nKeys and values:")
    for key, value in person.items():
        print(f"{key}: {value}")

# Nested For Loops
def nested_loops():
    print("\n5. Nested Loops:")
    # Creating a multiplication table
    for i in range(1, 4):
        for j in range(1, 4):
            print(f"{i} x {j} = {i*j}")
        print("----")

# For Loop with Break and Continue
def loop_control():
    print("\n6. Loop Control Statements:")
    # Break example
    print("Break when number is 3:")
    for num in range(1, 6):
        if num == 3:
            break
        print(num)
    
    # Continue example
    print("\nSkip number 3:")
    for num in range(1, 6):
        if num == 3:
            continue
        print(num)

# For Loop with else clause
def loop_with_else():
    print("\n7. For Loop with Else:")
    # Else executes when loop completes normally
    for i in range(3):
        print(i)
    else:
        print("Loop completed successfully!")
    
    # Else doesn't execute when loop breaks
    print("\nLoop with break:")
    for i in range(3):
        if i == 2:
            break
        print(i)
    else:
        print("This won't be printed!")

# List Comprehension
def list_comprehension():
    print("\n8. List Comprehension:")
    # Traditional way
    squares = []
    for x in range(5):
        squares.append(x**2)
    print(f"Traditional way: {squares}")
    
    # Using list comprehension
    squares_comp = [x**2 for x in range(5)]
    print(f"List comprehension: {squares_comp}")
    
    # List comprehension with condition
    even_squares = [x**2 for x in range(10) if x % 2 == 0]
    print(f"Even squares: {even_squares}")

# Main execution
if __name__ == "__main__":
    basic_list_loop()
    range_loop()
    enumerate_loop()
    dictionary_loop()
    nested_loops()
    loop_control()
    loop_with_else()
    list_comprehension()
