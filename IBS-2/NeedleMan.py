matrix = []
match = 2
mismatch = -1
gap = -2
seq1 = "ATGCA"; n1 = len(seq1)+1
seq2 = "AGCA"; n2 = len(seq2)+1
matrix = [[0] * n1 for _ in range(n2)]
for i in range(n2):
    matrix[i][0] = i * gap
for i in range(n1):
    matrix[0][i] = i * gap

for i in range(1,n1):
    for j in range(1,n2):
        diagonal = matrix[i-1][j-1]
        if seq1[j-1] == seq2[i-1]:
            diagonal += match
        else:
            diagonal += mismatch
        left = matrix[i-1][j] + gap
        up = matrix[i][j-1] + gap
        matrix[i][j] = max(diagonal, up, left)

for i in range(n1):
    print(matrix[i])

i = n2-1; j = n1-1
print(i,j)   
start = matrix[n1-1][n2-1]
s1 = ""; s2 = ""
while i!=0 and j!=0:
    if seq1[i-1] == seq2[j-1]:
        i-=1; j-=1
        s1+=seq1[i]; s2+=seq2[j]
    else:
        left = matrix[i-1][j]
        up = matrix[i][j-1]
        diagonal = matrix[i-1][j-1]
        L = [left, up, diagonal]
        if max(L) == left:
            j-=1
            s1+="_";s2+=seq2[j]
        elif max(L) == diagonal:
            i-=1; j-=1
            s1+=seq1[i]; s2+=seq2[j]
        else:
            i-=1
            s1+=seq1[i];s2+="_"



print(s1[::-1])
print(s2[::-1])







# # Dot Plot Matrix
# seq1 = "ATTAGC"
# seq2 = "ATAGC"
# matrix = [[0 for j in range(len(seq2))] for i in range(len(seq1))]
# # print(matrix)
# for i in range(len(seq1)):
#     for j in range(len(seq2)):
#         if seq1[i] == seq2[j]:
#             matrix[i][j] = 1
# for i in range(len(matrix)):
#     print(matrix[i])
    