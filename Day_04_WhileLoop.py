
# While Loop in Python
# A while loop executes a block of code repeatedly as long as a given condition is True

# Basic While Loop
print("Basic While Loop Example:")
count = 1
while count <= 5:
    print(count)
    count += 1

# While Loop with else statement
print("\nWhile Loop with else Example:")
num = 1
while num < 4:
    print(f"Inside loop: {num}")
    num += 1
else:
    print("Loop completed!")

# Break Statement in While Loop
print("\nBreak Statement Example:")
i = 1
while i <= 5:
    if i == 3:
        break
    print(i)
    i += 1
print("Loop broken!")

# Continue Statement in While Loop
print("\nContinue Statement Example:")
j = 0
while j < 5:
    j += 1
    if j == 3:
        continue
    print(j)

# Infinite Loop with user input
print("\nInput Control Loop Example:")
while True:
    user_input = input("Enter 'quit' to exit: ")
    if user_input.lower() == 'quit':
        break
    print(f"You entered: {user_input}")

# Nested While Loops
print("\nNested While Loops Example:")
outer = 1
while outer <= 3:
    inner = 1
    while inner <= 3:
        print(f"Outer: {outer}, Inner: {inner}")
        inner += 1
    outer += 1

# While Loop with List
print("\nWhile Loop with List Example:")
fruits = ['apple', 'banana', 'orange']
index = 0
while index < len(fruits):
    print(fruits[index])
    index += 1

# Flag Controlled While Loop
print("\nFlag Controlled While Loop Example:")
active = True
attempts = 0
while active:
    attempts += 1
    if attempts > 3:
        active = False
    print(f"Attempt {attempts}")

'''
Key Points about While Loops:
1. The loop continues as long as the condition is True
2. Make sure to include a way to exit the loop (avoid infinite loops)
3. The condition is checked at the beginning of each iteration
4. Use break to exit a loop prematurely
5. Use continue to skip the rest of the current iteration
6. while else executes when the loop condition becomes False
'''
