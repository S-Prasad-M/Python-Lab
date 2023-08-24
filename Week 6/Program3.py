L = eval(input("Ënter list: "))
a = int(input("Ënter number to search: "))
if a in L:
    print("Found at ",L.index(a)+1)
