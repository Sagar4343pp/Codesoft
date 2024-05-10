def calculator(num1,num2,operation):
    if operation == "+":
        total = num1 + num2
        return (f'{num1} + {num2} = {total}')
    elif operation == "-":
        total  = num1 - num2
        return (f'{num1} - {num2} = {total}')
    elif operation == "*":
        total  = num1 * num2
        return (f'{num1} * {num2} = {total}')
    elif operation == "/":
        total  = num1 / num2
        return (f'{num1} / {num2} = {total}')
    else:
        return ('Invalid Operation')
    
num1 = int(input("enter your Number:  "))
num2 = int(input("Enter your Number:    "))
operation = str(input('Enter operation (+,-,*,/,):  '))

print(calculator(num1,num2,operation))