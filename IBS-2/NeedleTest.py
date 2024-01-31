matrix = []
match = 2
mismatch = -1
gap = -2
seq1 = "ATGTA"
seq2 = "AGCA"

n1 = len(seq1) + 1
n2 = len(seq2) + 1

# Determine the longer sequence length
max_len = max(n1, n2)

# Initialize the matrix with appropriate dimensions
matrix = [[0] * max_len for _ in range(max_len)]

# Fill the matrix with appropriate initial values
for i in range(max_len):
    matrix[i][0] = i * gap
    matrix[0][i] = i * gap

# Fill the matrix following the algorithm
for i in range(1, n2):
    for j in range(1, n1):
        diagonal = matrix[i - 1][j - 1]
        if seq1[j - 1] == seq2[i - 1]:
            diagonal += match
        else:
            diagonal += mismatch
        left = matrix[i - 1][j] + gap
        up = matrix[i][j - 1] + gap
        matrix[i][j] = max(diagonal, up, left)

# Find the alignment
i = n2 - 1
j = n1 - 1
s1 = ""
s2 = ""

while i > 0 or j > 0:
    if i > 0 and j > 0 and seq1[j - 1] == seq2[i - 1]:
        s1 = seq1[j - 1] + s1
        s2 = seq2[i - 1] + s2
        i -= 1
        j -= 1
    elif i > 0 and (j == 0 or matrix[i][j] == matrix[i - 1][j] + gap):
        s1 = '_' + s1
        s2 = seq2[i - 1] + s2
        i -= 1
    else:
        s1 = seq1[j - 1] + s1
        s2 = '_' + s2
        j -= 1

print("Sequence 1:", s1)
print("Sequence 2:", s2)
