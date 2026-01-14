equation = input().strip()

if equation[0] == 'x':

    operand = int(equation[2])
    result = int(equation[4])
    if equation[1] == '+':
        print(result - operand)
    else:
        print(result + operand)

elif equation[2] == 'x':

    operand = int(equation[0])
    result = int(equation[4])
    if equation[1] == '+':
        print(result - operand)
    else:
        print(operand - result)

else:

    operand1 = int(equation[0])
    operand2 = int(equation[2])
    if equation[1] == '+':
        print(operand1 + operand2)
    else:
        print(operand1 - operand2)
