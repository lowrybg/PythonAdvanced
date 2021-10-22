rows = int(input())
matrix = []

for row in range(rows):
    matrix.append([int(x) if x.lstrip("-").isdigit() else x for x in input().split()])

flag = False
alice_coor = []
for row in range(rows):
    for col in range(rows):
        if matrix[row][col] == "A":
            alice_coor.append(row)
            alice_coor.append(col)
            flag = True
    if flag:
        break

end = False
win = False

move_coor = []
tea = 0
while True:
    dict_move = {"up": [alice_coor[0] - 1, alice_coor[1]],
                 "down": [alice_coor[0] + 1, alice_coor[1]],
                 "left": [alice_coor[0], alice_coor[1] - 1],
                 "right": [alice_coor[0], alice_coor[1] + 1]}
    command = input()
    if command in dict_move:
        move_coor.clear()
        move_coor.append(dict_move[command][0])
        move_coor.append(dict_move[command][1])


    if 0 <= move_coor[0] < rows and 0 <= move_coor[1] < rows:
        row = move_coor[0]
        col = move_coor[1]
        if matrix[row][col] == ".":
            matrix[alice_coor[0]][alice_coor[1]] = "*"
            alice_coor.clear()
            alice_coor.append(row)
            alice_coor.append(col)
        elif str(matrix[row][col]).lstrip().isdigit():
            tea += matrix[row][col]
            matrix[alice_coor[0]][alice_coor[1]] = "*"
            alice_coor.clear()
            alice_coor.append(row)
            alice_coor.append(col)
            if tea >= 10:
                win = True
                break
        elif matrix[row][col] == "*":
            matrix[alice_coor[0]][alice_coor[1]] = "*"
            alice_coor.clear()
            alice_coor.append(row)
            alice_coor.append(col)
        elif matrix[row][col] == "R":
            matrix[alice_coor[0]][alice_coor[1]] = "*"
            matrix[row][col] = "*"
            break
    else:
        break
if win:
    print("She did it! She went to the party.")
else:
    print("Alice didn't make it to the tea party.")

matrix[alice_coor[0]][alice_coor[1]] = "*"
for row in range(rows):
    for col in range(rows):
        print(matrix[row][col], end = " ")
    print()