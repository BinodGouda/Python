num1 = int(input())
num2 = int(input())
operator = input()


if(operator == '+'):
    sum = num1 + num2
    print(f"Sum of {num1} and {num2} = {sum}")
elif(operator == '-'):
    sum = num1 - num2
    print(f"Sum of {num1} and {num2} = {sum}")
elif(operator == '*'):
    sum = num1 * num2
    print(f"Sum of {num1} and {num2} = {sum}")
elif(operator == '/'):
    sum = num1 / num2
    print(f"Sum of {num1} and {num2} = {sum}")
