a = int(input("enter first number: "))
b = int(input("enter second number: "))
print("choose operation: +, -, *, /")
op = input("enter the operator: ")

match op:
    case '+':
        print("Addition:", a + b)
    case '-':
        print("Addition:", a - b)
    case '*':
        print("Addition:", a * b)
    case '/':
        print("Addition:", a / b)