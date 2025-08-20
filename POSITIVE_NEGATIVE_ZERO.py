n = int(input("Enter the number: "))

def check():
    if n > 0:
        print(n, "is positive number")
    elif n < 0:
        print(n, "is negative number")
    else:
        print(n, "is zero")
check()