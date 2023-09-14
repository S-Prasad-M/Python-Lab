n = int(input("Ënter number to find factorial: "))
fact = 1
for i in range(2,n+1):
    fact *= i
print("Factorial = ",fact)