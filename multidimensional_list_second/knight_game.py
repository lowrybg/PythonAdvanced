import sys
from io import StringIO

test_input_one = """5 
0K0K0
K000K
00K00
K000K
0K0K0
"""
test_input_two = """"""

sys.stdin = StringIO(test_input_one)
# sys.stdin = StringIO(test_input_two)

size = int(input())
matrix = []

for _ in range(size):
    matrix.append(list(input()))


def is_inside(len_mat, row, col):
    if 0 <= row < len_mat and 0 <= col < len_mat:
        return True
    return False


def attacker_count(mat, a_r, a_c):
    count = 0
    if is_inside(size, a_r + 2, a_c - 1) and mat[a_r + 2][a_c - 1] == "K":
        count += 1
    if is_inside(size, a_r + 1, a_c - 2) and mat[a_r + 1][a_c - 2] == "K":
        count += 1
    if is_inside(size, a_r - 1, a_c - 2) and mat[a_r - 1][a_c - 2] == "K":
        count += 1
    if is_inside(size, a_r - 2, a_c - 1)and mat[a_r - 2][a_c - 1] == "K":
                count += 1
    if is_inside (size, a_r - 2, a_c + 1) and mat[a_r - 2][a_c + 1] == "K":
        count += 1
    if is_inside (size, a_r - 1, a_c + 2) and mat[a_r - 1][a_c + 2] == "K":
        count += 1
    if is_inside(size, a_r + 1, a_c + 2) and mat[a_r + 1][a_c + 2] == "K":
        count += 1
    if is_inside(size, a_r + 2, a_c + 1) and mat[a_r + 2][a_c + 1] == "K":
        count += 1
    return count


removed_knights = 0
while True:
    max_count = 0
    affected_knights = 0
    max_attacker_row = 0
    max_attacker_col = 0

    for r in range(size-1):
        for c in range(size-1):
            if matrix[r][c] == "K":
                affected_knights = attacker_count(matrix, r, c)
            if affected_knights > max_count:
                max_count = affected_knights
                max_attacker_row, max_attacker_col = r, c
    if not max_count == 0:
        matrix[max_attacker_row][max_attacker_col] = "0"
        removed_knights += 1
    if affected_knights == 0:
        break

print(removed_knights)

#
# def attack_number(matr,row,col):
#     k_moves = [
#         [row-1,col-2],
#         [row-2,col-1],
#         [row-2,col+1],
#         [row-1,col+2],
#         [row+1,col+2],
#         [row+2,col+1],
#         [row+2,col-1],
#         [row+1,col-2]]
#     numbers_of_attack = 0
#     for move in k_moves:
#         r,c= move[0],move[1]
#         if r >= 0 and  c >= 0:
#             if r < len(matr) and c < len(matr):
#                 if matrix[r][c] == 'K':
#                     numbers_of_attack+=1
#
#     return int(numbers_of_attack)
#
# rows = int(input())
# matrix = []
#
# for row in range(rows):
#     current_row = input()
#     matrix.append([])
#     matrix[row] = [el for el in current_row]
#
# biggest_attacker = None
# attacker_pos = []
# count = 0
# while not biggest_attacker == 0:
#     biggest_attacker = 0
#     for i in range(rows):
#         for j in range(rows):
#             if matrix[i][j] == 'K':
#                 current_k = attack_number(matrix,i,j)
#                 if current_k > biggest_attacker:
#                     biggest_attacker = current_k
#                     attacker_pos.clear()
#                     attacker_pos.append(int(i))
#                     attacker_pos.append(int(j))
#     if biggest_attacker == 0:
#         break
#     else:
#         r, c = attacker_pos[0],attacker_pos[1]
#         matrix[r][c] = 0
#         count +=1
#         attacker_pos.clear()
#
# print(count)
