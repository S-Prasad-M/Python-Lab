tup=(1,2,3,4,5,'a','bb','c','xyz')
print("Items inatuple")
for i in tup:
    print(i,end=" ")
print("\nLength of tuple",len(tup))
i=int(input("enter a value"))
print(i in tup)
tup[1]="hello"
print(tup)