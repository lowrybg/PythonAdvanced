import sys
from io import StringIO

test_input_one = """2 3
1 2 3
4 5 6
swap 0 0 1 1
swap 10 9 8 7
swap 0 1 1 0
END
"""
test_input_two = """1 2
Hello World
0 0 0 1
swap 0 0 0 1
swap 0 1 0 0
END
"""

# sys.stdin = StringIO(test_input_one)
# sys.stdin = StringIO(test_input_two)

rows_n, cols_n = [int(x) for x in input().split()]

matrix = []
for _ in range(rows_n):
    matrix.append([(x) for x in input().split()])

lines = input().split()

while not lines[0] == "END":
    if len(lines) == 5 and lines[0] == 'swap':
        try:
            c_row, c_col, next_row, next_col = [int(x) for x in lines[1:]]
        except ValueError:

            continue
        if 0<= c_row <= rows_n and 0 <= c_col <= cols_n:
            matrix[c_row][c_col], matrix[next_row][next_col] =matrix[next_row][next_col], matrix[c_row][c_col]
            for r in range(rows_n):
                print(*matrix[r])
        else:
            print('Invalid input!')
    else:
        print('Invalid input!')
    lines = input().split()