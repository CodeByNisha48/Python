# search for numbers in this tuples using loop

tup = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
x = 36
i = 0
while (i <= len(tup)):
    if(tup[i] == x):
        print("found at index", i)
        break
    else:
        print("finding...")
    i += 1