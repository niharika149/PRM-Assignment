size = int(input("Enter the size of the list : ")) # number of elements in the list
lst = [input("Enter the words : ") for _ in range(size)] # create the list
lst.sort(key = lambda x: x[-2] if len(x) >1 else x) # sort the list based on 2nd last character of each string
print(lst)