n = int(input("Enter the number: "))

def Factorial():
    fact = 1
    for val in range(1, n+1):
        fact *= val
    print("Factorial of", n,"is:",fact)
Factorial()