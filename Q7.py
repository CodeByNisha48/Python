# Search for a number x in this tuple using loop:

tup = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 49)
i = 0
x = 49
for val in tup:
    if(val == x):
        print("found at index", i)
    i += 1