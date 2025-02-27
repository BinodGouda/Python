# Day_01_Operators.py

# Python Operators
# Operators are used to perform operations on variables and values.

# In the example below, we use the + operator to add together two values:
print("Addition Example: ", 10 + 5)  # Output: 15

# Python divides the operators in the following groups:
# Arithmetic operators
# Assignment operators
# Comparison operators
# Logical operators
# Identity operators
# Membership operators
# Bitwise operators

# Python Arithmetic Operators
# Arithmetic operators are used with numeric values to perform common mathematical operations:
# Operator    Name            Example        Output
# +           Addition        x + y          15
# -           Subtraction     x - y          5
# *           Multiplication  x * y          50
# /           Division        x / y          2.0
# %           Modulus         x % y          0
# **          Exponentiation  x ** y         100000
# //          Floor division  x // y         2

x = 10
y = 5
print("Arithmetic Operators:")
print("Addition: ", x + y)          # Output: 15
print("Subtraction: ", x - y)       # Output: 5
print("Multiplication: ", x * y)    # Output: 50
print("Division: ", x / y)          # Output: 2.0
print("Modulus: ", x % y)           # Output: 0
print("Exponentiation: ", x ** y)   # Output: 100000
print("Floor Division: ", x // y)    # Output: 2

# Python Assignment Operators
# Assignment operators are used to assign values to variables:
# Operator    Example         Same As        Output
# =           x = 5          x = 5
# +=          x += 3         x = x + 3     8
# -=          x -= 3         x = x - 3     2
# *=          x *= 3         x = x * 3     15
# /=          x /= 3         x = x / 3     5.0
# %=          x %= 3         x = x % 3     2
# //=         x //= 3        x = x // 3    0
# **=         x **= 3        x = x ** 3    0
# &=          x &= 3         x = x & 3     0
# |=          x |= 3         x = x | 3     3
# ^=          x ^= 3         x = x ^ 3     3
# >>=         x >>= 3        x = x >> 3    0
# <<=         x <<= 3        x = x << 3    0
# :=          print(x := 3)  x = 3         3

x = 5
print("\nAssignment Operators:")
x += 3  # x = x + 3
print("x += 3: ", x)  # Output: 8
x -= 3  # x = x - 3
print("x -= 3: ", x)  # Output: 5
x *= 3  # x = x * 3
print("x *= 3: ", x)  # Output: 15
x /= 3  # x = x / 3
print("x /= 3: ", x)  # Output: 5.0

# Floor Division Assignment
x1 = 10
x1 //= 3  # Equivalent to x = x // 3
print("After x //= 3:", x1)  # Output: 3 (10 // 3 = 3)

# Exponentiation Assignment
x1 **= 2  # Equivalent to x = x ** 2
print("After x **= 2:", x1)  # Output: 9 (3 ** 2 = 9)

# Bitwise AND Assignment

x1 &= 3  # Equivalent to x = x & 3
print("After x &= 3:", x1)  # Output: 1 (9 & 3 = 1)

# Bitwise OR Assignment
x1 |= 3  # Equivalent to x = x | 3
print("After x |= 3:", x1)  # Output: 3 (1 | 3 = 3)

# Bitwise XOR Assignment
x1 ^= 3  # Equivalent to x = x ^ 3
print("After x ^= 3:", x1)  # Output: 0 (3 ^ 3 = 0)

# Bitwise Right Shift Assignment
x1 = 8  # Reset x to 8
print("Reset x to:", x1)  # Output: 8
x1 >>= 2  # Equivalent to x = x >> 2
print("After x >>= 2:", x1)  # Output: 2 (8 >> 2 = 2)

# Bitwise Left Shift Assignment
x = 1  # Reset x to 1
print("Reset x to:", x)  # Output: 1
x <<= 3  # Equivalent to x = x << 3
print("After x <<= 3:", x)  # Output: 8 (1 << 3 = 8)

# Assignment Expression
print("Using walrus operator:", (x := 3))  # Output: 3 (assigns 3 to x and prints it)
print("Value of x after assignment:", x)  # Output: 3

# Python Comparison Operators
# Comparison operators are used to compare two values:
# Operator    Name            Example        Output
# ==          Equal           x == y         False
# !=          Not equal       x != y         True
# >           Greater than    x > y          True
# <           Less than       x < y          False
# >=          Greater than or equal to x >= y  True
# <=          Less than or equal to x <= y   False

print("\nComparison Operators:")
x=5
print("x == 5: ", x == 5)          # Output: True
print("x != 5: ", x != 5)          # Output: False
print("x > 3: ", x > 3)            # Output: True
print("x < 10: ", x < 10)          # Output: True
print("x >= 5: ", x >= 5)          # Output: True
print("x <= 5: ", x <= 5)          # Output: True

# Python Logical Operators
# Logical operators are used to combine conditional statements:
# Operator    Description      Example        Output
# and         Returns True if both statements are true x < 10 and x > 5  True
# or          Returns True if one of the statements is true x < 5 or x < 10  True
# not         Reverse the result, returns False if the result is true not(x < 5 and x < 10)  True

print("\nLogical Operators:")
print("x : ",x)
print("x < 10 and x > 5: ", (x < 10 and x > 5))  # Output: True
print("x < 5 or x < 10: ", (x < 5 or x < 10))    # Output: True
print("not (x < 5 and x < 10): ", not (x < 5 and x < 10))  # Output: True

# Python Identity Operators
# Identity operators are used to compare the objects, not if they are equal, but if they are actually the same object, with the same memory location:
# Operator    Description      Example        Output
# is          Returns True if both variables are the same object x is y
# is not      Returns True if both variables are not the same object x is not y

a = [1, 2, 3]
b = a
c = list(a)

print("\nIdentity Operators:")
print("a is b: ", a is b)          # Output: True
print("a is c: ", a is c)          # Output: False
print("a is not c: ", a is not c)  # Output: True

# Python Membership Operators
# Membership operators are used to test if a value is in a sequence:
# Operator    Description      Example        Output
# in          Returns True if a sequence with the specified value is present in the object x in y
# not in      Returns True if a sequence with the specified value is not present in the object x not in y

my_list = [1, 2, 3, 4, 5]

print("\nMembership Operators:")
print("3 in my_list: ", 3 in my_list)          # Output: True
print("6 not in my_list: ", 6 not in my_list)  # Output: True

# Python Bitwise Operators
# Bitwise operators are used to compare (binary) numbers:
# Operator    Name            Description     Example        Output
# &           AND             Sets each bit to 1 if both bits are 1 x & y
# |           OR              Sets each bit to 1 if one of two bits is 1 x | y
# ^           XOR             Sets each bit to 1 if only one of two bits is 1 x ^ y
# ~           NOT             Inverts all the bits ~x
# <<          Zero fill left shift Shift left by pushing zeros in from the right and let the leftmost bits fall off x << 2
# >>          Signed right shift Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off x >> 2

x = 5  # (binary: 0101)
y = 3  # (binary: 0011)

print("\nBitwise Operators:")
print("x & y: ", x & y)  # Output: 1 (binary: 0001)
print("x | y: ", x | y)  # Output: 7 (binary: 0111)
print("x ^ y: ", x ^ y)  # Output: 6 (binary: 0110)
print("~x: ", ~x)        # Output: -6 (inverts bits)
print("x << 1: ", x << 1)  # Output: 10 (binary: 1010)
print("x >> 1: ", x >> 1)  # Output: 2 (binary: 0010)

# Operator Precedence
# Operator precedence describes the order in which operations are performed.
# Example
# Parentheses has the highest precedence, meaning that expressions inside parentheses must be evaluated first:
print("\nOperator Precedence:")
print("Result of (6 + 3) - (6 + 3): ", (6 + 3) - (6 + 3))  # Output: 0

# Example
# Multiplication * has higher precedence than addition +, and therefore multiplications are evaluated before additions:
print("Result of 100 + 5 * 3: ", 100 + 5 * 3)  # Output: 115

# The precedence order is described in the table below, starting with the highest precedence at the top:
# Operator                      Description      
# ()                            Parentheses
# **                            Exponentiation
# +x  -x  ~x                    Unary plus, unary minus, and bitwise NOT
# *  /  //  %                   Multiplication, division, floor division, and modulus
# +  -                          Addition and subtraction
# <<  >>                        Bitwise left and right shifts
# &                             Bitwise AND
# ^                             Bitwise XOR
# |                             Bitwise OR
# ==  !=  >  >=  <  <=          is  is not  in  not in  Comparisons, identity, and membership operators
# not                           Logical NOT
# and                           AND
# or                            OR

# If two operators have the same precedence, the expression is evaluated from left to right.
# Example
# Addition + and subtraction - has the same precedence, and therefore we evaluate the expression from left to right:
print("Result of 5 + 4 - 7 + 3: ", 5 + 4 - 7 + 3)  # Output: 5
