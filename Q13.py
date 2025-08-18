# WAP to find the sum of first natural numbers. (using for loop)

n = int(input("Enter the number: "))
sum = 0
for i in range(1, n+1):
    sum += i
print("Total sum:",sum)