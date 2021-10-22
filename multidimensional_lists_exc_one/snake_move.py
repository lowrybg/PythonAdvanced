rows, cols = [int(x) for x in input().split()]
line = input()

index = 0
matrix = []
for row in range(rows):
    matrix.append([None]*cols)
    for col in range(cols):
        if row % 2 == 0:
            matrix[row][col] = line[index]
        else:
            matrix[row][cols - 1 - col] = line[index]
        index = (index +1 ) % len(line)

for el in matrix:
    print(''.join(el))