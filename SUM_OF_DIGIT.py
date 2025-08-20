def show(x):
    total = 0
    while x > 0:
        digit = x % 10
        x = x // 10
        total = total + digit
    return total

x = int(input("Enter a number: "))
print("Sum of digits:", show(x))
