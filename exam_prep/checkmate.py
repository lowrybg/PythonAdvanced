import sys
from io import StringIO

test_input_one = """. . . . . . . .
Q . . . . . . .
. K . . . Q . .
. . . Q . . . .
Q . . . Q . . .
. Q . . . . . .
. . . . . . Q .
. Q . Q . . . .
"""
test_input_two = """"""

sys.stdin = StringIO(test_input_one)
# sys.stdin = StringIO(test_input_two)


def is_in_range (row, col, n):
    if 0 <= row <= n and 0 <= col <= n:
        return True
    return False

moves = {
    'up': (-1,0),
    'down': (1,0),
    'left': (0,-1),
    'right': (0,1),
    'ver_up_left': (-1,-1),
    'ver_down_left': (1,-1),
    'ver_up_right': (-1,1),
    'ver_down_right': (1,1),

}



b = 8
board = [input().split(' ') for _ in range(b)]
knight = ()
for r in range(b):
    for c in range(b):
        if board[r][c] == "K":
            knight = r,c

a=3