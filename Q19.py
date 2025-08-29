#Write a recursive function to calculate the sum of first n natural number.

def print_sum(n):
    if(n == 0):
        return 0
    return print_sum(n-1) + n
sum = print_sum(5)
print(sum)