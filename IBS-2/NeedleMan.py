matrix = []
match = 2
mismatch = -1
gap = -2
seq1 = "ATGCA"; n1 = len(seq1)+1
seq2 = "AGCAA"; n2 = len(seq2)+1
matrix = [[0] * n1 for _ in range(n2)]
for i in range(n2):
    matrix[i][0] = i * gap
for i in range(n1):
    matrix[0][i] = i * gap

for i in range(1,n2):
    for j in range(1,n1):
        diagonal = matrix[i-1][j-1]
        if seq1[i-1] == seq2[j-1]:
            diagonal += match
        else:
            diagonal += mismatch
        left = matrix[i][j-1] + gap
        up = matrix[i - 1][j] + gap
        matrix[i][j] = max(diagonal, up, left)

for i in range(n1):
    print(matrix[i])

i = n1-1; j = n2-1
# print(i,j)   
start = matrix[n1-1][n2-1]
s1 = ""; s2 = ""
while i!=0 and j!=0:
    if seq1[i-1] == seq2[j-1]:





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
    