import sys
from io import StringIO

test_input_one = """3
1 2 3
4 5 6
7 8 9
Add 0 0 5
Subtract 1 1 2
END
"""
test_input_two = """"""

# sys.stdin = StringIO(test_input_one)
# sys.stdin = StringIO(test_input_two)

rows_n = int(input())

matrix = []
for _ in range(rows_n):
    matrix.append([int(x) for x in input().split()])

lines = input().split()

while not lines[0] == "END":
    if len(lines) == 4 and lines[0] == 'Add':
        try:
            c_row, c_col, mod_value = [int(x) for x in lines[1:]]
        except ValueError:
            continue
        if 0<= c_row < rows_n and 0<= c_col < rows_n :
            matrix[c_row][c_col] += mod_value
        else:
            print('Invalid coordinates')
    elif len(lines) == 4 and lines[0] == 'Subtract':
        try:
            c_row, c_col, mod_value = [int(x) for x in lines[1:]]
        except ValueError:
            continue
        if 0 <= c_row < rows_n and 0<= c_col < rows_n :
            matrix[c_row][c_col] -= mod_value
        else:
            print('Invalid coordinates')

    lines = input().split()

for r in range(rows_n):
    print(*matrix[r])