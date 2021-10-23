import sys
from io import StringIO

test_input_one = """5
1 X 7 9 11
X 14 46 62 0
15 33 21 95 X
P 14 3 4 18
9 20 33 X 0
right
right
up
up
left
down
"""
test_input_two = """8
13 18 9 7 24 41 52 11
54 21 19 X 6 4 75 6
76 5 7 1 76 27 2 37
92 3 25 37 52 X 56 72
15 X 1 45 45 X 7 63
1 63 P 2 X 43 5 1
48 19 35 20 100 27 42 80
73 88 78 33 37 52 X 22
up
left
"""

# sys.stdin = StringIO(test_input_one)
# sys.stdin = StringIO(test_input_two)

size = int(input())

matrix = []

player_row = 0
player_col = 0
for row in range(size):
    matrix.append(input().split())
    for col in range(size):
        if matrix[row][col] == "P":
            player_row = row
            player_col = col
moves = {
    'up': lambda r, c: (r-1,c),
    'down': lambda r, c: (r+1,c),
    'left': lambda r, c: (r, c - 1),
    'right': lambda r, c: (r, c + 1),
}


def is_inside(len_mat, r, c):
    return 0 <= r < len_mat and 0 <= c < len_mat


positions = []
coins = 0
next_row, next_col = player_row, player_col
while True:
    line = input()
    next_row, next_col = moves[line](next_row,next_col)
    if is_inside(size,next_row, next_col) and not matrix[next_row][next_col] == "X":
        coins += int(matrix[next_row][next_col])
        positions.append([next_row,next_col])
        if coins >= 100:
            print(f'You won! You\'ve collected {coins} coins.')
            break
    else:
        print(f'Game over! You\'ve collected {coins//2} coins.')
        break
print('Your path:')
for el in positions:
    print(el)

