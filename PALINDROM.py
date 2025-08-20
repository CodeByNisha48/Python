a = input("Enter the number check palindrome: ")

def palindrom(a):
    b = ""                         
    for char in a:
        b = char + b               
        print(b)                  

    if a == b:                     
        print(a,"is palindrome")
    else:
        print(a,"is not palindrome")

palindrom(a)
