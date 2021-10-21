n = int(input())

primary = []
secondary = []

matrix = []
for _ in range(n):
    matrix.append([int(x) for x in input().split(', ')])

for r in range(n):
    primary.append(matrix[r][r])
    secondary.append(matrix[r][n - 1 -r])

print(f'Primary diagonal: {", ".join([str(x) for x in primary])}. Sum: {sum(primary)}')

print(f'Secondary diagonal: {", ".join([str(x) for x in secondary])}. Sum: {sum(secondary)}')
