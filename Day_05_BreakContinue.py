
"""
Break and Continue Statements in Python

1. Break Statement: 
   - Terminates the loop prematurely
   - Exits the entire loop when encountered
   - Used in both while and for loops

2. Continue Statement:
   - Skips the rest of the current iteration
   - Moves to the next iteration
   - Used in both while and for loops
"""

# Break Statement Examples
print("1. Break Statement Examples:")

# Example 1: Break in a for loop
print("\nExample 1.1 - Break in for loop:")
for i in range(1, 6):
    if i == 4:
        break
    print(f"Current number: {i}")

# Example 2: Break in while loop
print("\nExample 1.2 - Break in while loop:")
counter = 1
while counter <= 5:
    if counter == 3:
        break
    print(f"Counter value: {counter}")
    counter += 1

# Example 3: Break in nested loops
print("\nExample 1.3 - Break in nested loops:")
for outer in range(1, 4):
    print(f"Outer loop: {outer}")
    for inner in range(1, 4):
        if inner == 2:
            break
        print(f"  Inner loop: {inner}")

# Continue Statement Examples
print("\n2. Continue Statement Examples:")

# Example 1: Continue in for loop
print("\nExample 2.1 - Continue in for loop:")
for i in range(1, 6):
    if i == 3:
        continue
    print(f"Number: {i}")

# Example 2: Continue in while loop
print("\nExample 2.2 - Continue in while loop:")
count = 0
while count < 5:
    count += 1
    if count == 2:
        continue
    print(f"Count: {count}")

# Example 3: Continue with string iteration
print("\nExample 2.3 - Continue with string:")
text = "Python"
for char in text:
    if char in 'yo':  # Skip 'y' and 'o'
        continue
    print(f"Character: {char}")

# Practical Examples
print("\n3. Practical Examples:")

# Example 1: Break with user input
print("\nExample 3.1 - Number guessing with break:")
secret_number = 5
while True:
    guess = int(input("Guess the number (1-10): "))
    if guess == secret_number:
        print("Correct guess!")
        break
    print("Try again!")

# Example 2: Continue with number filtering
print("\nExample 3.2 - Filtering even numbers:")
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Printing only odd numbers:")
for num in numbers:
    if num % 2 == 0:
        continue
    print(num)

"""
Key Points to Remember:
1. Break:
   - Use break when you want to exit a loop completely
   - Useful for early termination based on a condition
   - Often used in infinite loops with a condition

2. Continue:
   - Use continue to skip specific iterations
   - The loop continues with the next iteration
   - Helpful for filtering out unwanted values

3. Best Practices:
   - Use break and continue sparingly for better code readability
   - Consider using regular loop conditions when possible
   - Document the usage of break/continue for clarity
"""
