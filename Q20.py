def print_list(mylist, idx):
    if idx == len(mylist):   
        return
    print(mylist[idx])
    print_list(mylist, idx+1)

fruits = ["mango", "litchi", "apple", "banana"]
print_list(fruits, 0)  
