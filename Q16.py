#WAF to find the factorial of n. (n is the parameter)


def calc_fact(n):
    fact = 1
    for val in range(1, n+1):
        fact *= val
    return fact
n = 5
print(calc_fact(n))