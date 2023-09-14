n = int(input("Ënter n: "))
L = []
print("Ënter numbers:")
for i in range(n):
    L.append(int(input()))
sum = 0
for i in L:
    sum += i
print("List = ", L, "Sum = ",sum)