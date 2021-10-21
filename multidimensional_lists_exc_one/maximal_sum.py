import sys
from io import StringIO

test_input_one = """4 5
1 5 5 2 4
2 1 4 14 3
3 7 11 2 8
4 8 12 16 4

"""
test_input_two = """5 6
1 0 4 3 1 1
1 3 1 3 0 4
6 4 1 2 5 6
2 2 1 5 4 1
3 3 3 6 0 5
"""

sys.stdin = StringIO(test_input_one)
# sys.stdin = StringIO(test_input_two)

rows, cols = [int(x) for x in input().split()]
matrix = []

for _ in range(rows):
    matrix.append([int(x) for x in input().split()])

max_matrix = []


def search_square(matrix, row, col):
    global max_matrix
    max_sum = 0
    for i in range(row - 2):
        for j in range(col - 2):
            temp_sum = (matrix[i][j] + matrix[i][j + 1] + matrix[i + 1][j] + matrix[i + 1][j + 1] + \
                           matrix[i][j + 2] + matrix[i+2][j] + matrix[i + 2][j+1] + matrix[i + 2][j + 2] + matrix[i+1][j+2])
            if temp_sum > max_sum:
                max_sum = temp_sum
                max_matrix = []
                max_matrix.extend([i])
                max_matrix.extend([j])

    return max_sum


print(f'Sum = {search_square(matrix, rows, cols)}')
for row in range(max_matrix[0], max_matrix[0]+3):
    for col in range(max_matrix[1],max_matrix[1]+3):
        print(f'{matrix[row][col]} ', end='')
    print()
