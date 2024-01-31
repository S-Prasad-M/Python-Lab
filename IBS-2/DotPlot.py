seq1 = "ATGCA"
seq2 = "ATTGGCA"
n1 = len(seq1); n2 = len(seq2)
matrix = [[0]*n2 for _ in range(n1)]
for i in range(n1):
    for j in range(n2):
        if seq1[i]==seq2[j]:
            matrix[i][j] = 1
for i in matrix:
    print(i)

i = n2 - 1; j = n1 - 1
s1 = ""; s2 = ""
while i > 0 or j > 0:
    if i > 0 and j > 0 and seq1[j - 1] == seq2[i - 1]:
        s1 = seq1[j - 1] + s1
        s2 = seq2[i - 1] + s2
        i -= 1; j -= 1
