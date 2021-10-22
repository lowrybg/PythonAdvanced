import sys
from io import StringIO
import math

test_input_one = """5
1 3 7 9 11
X 5 4 X 63
7 3 21 95 1
B 1 73 4 9
9 2 33 2 0
"""
test_input_two = """8
4 18 9 7 24 41 52 11
54 21 19 X 6 34 75 57
76 67 7 44 76 27 56 37
92 35 25 37 52 34 56 72
35 X 1 45 4 X 37 63
105 X B 2 12 43 5 19
48 19 35 20 32 27 42 4
73 88 78 32 37 52 X 22
"""

# sys.stdin = StringIO(test_input_one)
# sys.stdin = StringIO(test_input_two)

size = int(input())

matrix = []

bunny_row = 0
bunny_col = 0

for row in range(size):
    matrix.append(input().split())
    for col in range(size):
        if matrix[row][col] == "B":
            bunny_row = row
            bunny_col = col

moves = {
    'up': lambda r, c: (r-1,c),
    'down': lambda r, c: (r+1,c),
    'left': lambda r, c: (r, c - 1),
    'right': lambda r, c: (r, c + 1),
}


def is_inside(len_mat, r, c):
    return 0 <= r < len_mat and 0 <= c < len_mat


max_value = float('-inf')
max_move = ''
max_matrix = []
for dir, move in moves.items():
    egs = 0
    next_row, next_col = move(bunny_row, bunny_col)
    temp_matrix = [[next_row, next_col]]
    while True:
        if not is_inside(size, next_row, next_col):
            break
        if matrix[next_row][next_col] == "X":
            break
        egs += int(matrix[next_row][next_col])
        if egs > max_value:
            max_value = egs
            max_move = dir
            temp_matrix.append([next_row,next_col])
            max_matrix = temp_matrix
        next_row, next_col = move(next_row, next_col)

if max_move:
    print(max_move)
for el in max_matrix:
    print(el)
if not max_value == float('-inf'):
    print(max_value)




