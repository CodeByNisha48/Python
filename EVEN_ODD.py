def calc_even_odd(num):
    if (num % 2 == 0):
        print(num, "is even number")
    else:
        print(num, "is odd number")

num = int(input("Enter the number: "))
calc_even_odd(num)
