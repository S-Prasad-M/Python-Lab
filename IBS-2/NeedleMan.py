matrix = []
match = 2
mismatch = -1
gap = -2
seq1 = "ATGCA"; n1 = len(seq1)
seq2 = "AGCAA"; n2 = len(seq2)
matrix = [[0] * n1 for _ in range(n2)]
for i in range(n2):
    matrix[i][0] = i * mismatch
for i in range(n1):
    matrix[0][i] = i * mismatch
for i in range(n2):
    for j in range(n1):
        diagonal = 0
        