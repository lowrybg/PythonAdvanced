n = int(input())

primary = []
secondary = []

matrix = []
for _ in range(n):
    matrix.append([int(x) for x in input().split()])

for r in range(n):
    primary.append(matrix[r][r])
    secondary.append(matrix[r][n - 1 -r])

sum_p = (sum([x for x in primary]))
sum_s = (sum([x for x in secondary]))
print(abs(sum_p-sum_s))