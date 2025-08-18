# Print the multiplication table of a number n.

n = int(input("Enter the number: "))

for i in range(1, 11):
    print(i , "x", n, "=", (i*n))