# print the multiplication table of a number n.

n = int(input("Enter the number: "))
x = 1
while (x <= 10):
    print(n, "x", x, "=", (n*x))
    x += 1