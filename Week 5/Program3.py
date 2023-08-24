a = int(input("Ënter number 1: "))
b = int(input("Ënter number 2: "))
sym = input("Ënter operator:")
if (sym == '+'):
    print("Sum = ",a+b)
elif (sym == '-'):
    print("Difference = ",a-b)
elif(sym == "*"):
    print("Multiplied = ", a*b )
elif(sym == "/"):
    print("Divided = ", a/b)
else:
    print("Invalid symbol")