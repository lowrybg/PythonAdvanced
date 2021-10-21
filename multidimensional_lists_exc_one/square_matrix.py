import sys
from io import StringIO

test_input_one = """3 4
A B B D
E B B B
I J B B
"""
test_input_two = """5 4
A A B D
A A B B
I J B B
C C C G
C C K P
"""

# sys.stdin = StringIO(test_input_one)
# sys.stdin = StringIO(test_input_two)

rows, cols = [int(x) for x in input().split()]
matrix = []

for _ in range(rows):
    matrix.append(input().split())


# deltas = [
#     (0, 0),
#     (0, 1),
#     (1, 0),
#     (1, 1),
# ]


def search_square(matrix,row,col):
    counter = 0
    for i in range(row - 1):
        for j in range(col - 1):
            if matrix[i][j] == matrix[i][j+1] == matrix[i+1][j] == matrix[i+1][j+1]:
                counter += 1
    return counter


print(search_square(matrix,rows,cols))