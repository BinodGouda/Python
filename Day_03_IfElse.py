"""
Python Conditional Statements (If-Else) Tutorial
=============================================
This module covers everything you need to know about conditional statements in Python.
"""

# 1. Basic if Statement
print("\n1. Basic if Statement:")
print("=" * 40)

age = 18
if age >= 18:
    print("You are an adult")
    print("You can vote")

# 2. if-else Statement
print("\n2. if-else Statement:")
print("=" * 40)

age = 16
if age >= 18:
    print("You are an adult")
else:
    print("You are a minor")

# 3. if-elif-else Statement (Multiple Conditions)
print("\n3. if-elif-else Statement:")
print("=" * 40)

score = 85
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")

# 4. Nested if Statements
print("\n4. Nested if Statements:")
print("=" * 40)

age = 25
has_license = True

if age >= 18:
    print("Age requirement met")
    if has_license:
        print("You can drive")
    else:
        print("You need a license to drive")
else:
    print("You are too young to drive")

# 5. Conditional Expressions (Ternary Operator)
print("\n5. Conditional Expressions:")
print("=" * 40)

age = 20
status = "adult" if age >= 18 else "minor"
print(f"Status: {status}")

# 6. Multiple Conditions using Logical Operators
print("\n6. Multiple Conditions:")
print("=" * 40)

age = 22
has_id = True
has_ticket = True

# Using and operator
if age >= 18 and has_id:
    print("You can enter the venue")

# Using or operator
if has_ticket or has_id:
    print("You can attend the event")

# Using not operator
if not has_ticket:
    print("You need to buy a ticket")

# 7. Checking Multiple Values
print("\n7. Checking Multiple Values:")
print("=" * 40)

# Using in operator
fruit = "apple"
if fruit in ["apple", "banana", "orange"]:
    print(f"{fruit} is in the fruit basket")

# Using comparison operators
number = 5
if 0 <= number <= 10:
    print(f"{number} is between 0 and 10")

# 8. Pattern Matching (Python 3.10+)
print("\n8. Pattern Matching (Python 3.10+):")
print("=" * 40)

def check_type(value):
    match value:
        case str():
            print(f"{value} is a string")
        case int():
            print(f"{value} is an integer")
        case list():
            print(f"{value} is a list")
        case _:
            print("Unknown type")

check_type("Hello")
check_type(42)
check_type([1, 2, 3])

# 9. Common Patterns and Best Practices
print("\n9. Common Patterns and Best Practices:")
print("=" * 40)

# Truth Value Testing
name = ""
if not name:    # Empty string is False
    print("Name is empty")

numbers = []
if not numbers:  # Empty list is False
    print("List is empty")

# Using is for None comparison
value = None
if value is None:
    print("Value is None")

# 10. Complex Conditions Example
print("\n10. Complex Conditions Example:")
print("=" * 40)

def check_eligibility(age, income, credit_score):
    """Example of complex nested conditions"""
    if age >= 18:
        if income >= 30000:
            if credit_score >= 700:
                return "Fully eligible"
            elif credit_score >= 600:
                return "Conditionally eligible"
            else:
                return "Not eligible - Low credit score"
        else:
            return "Not eligible - Income too low"
    else:
        return "Not eligible - Age requirement not met"

print(check_eligibility(25, 35000, 750))
print(check_eligibility(20, 25000, 650))
print(check_eligibility(17, 40000, 800))

# 11. Switch-Case Alternative (Dictionary Mapping)
print("\n11. Switch-Case Alternative:")
print("=" * 40)

def get_day_type(day):
    return {
        'Monday': 'Weekday',
        'Tuesday': 'Weekday',
        'Wednesday': 'Weekday',
        'Thursday': 'Weekday',
        'Friday': 'Weekday',
        'Saturday': 'Weekend',
        'Sunday': 'Weekend'
    }.get(day, 'Invalid day')

print(f"Monday is a {get_day_type('Monday')}")
print(f"Sunday is a {get_day_type('Sunday')}")

# 12. Error Handling with if-else
print("\n12. Error Handling with if-else:")
print("=" * 40)

def divide_numbers(a, b):
    if b == 0:
        return "Error: Division by zero"
    else:
        return a / b

print(divide_numbers(10, 2))
print(divide_numbers(10, 0))
