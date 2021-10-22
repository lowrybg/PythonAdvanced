
def get_houses_in_range(size, r, c):
    houses = []
    if is_inside(size, r - 1, c):
        houses.append([r - 1, c])
    if is_inside(size, r + 1, c):
        houses.append([r + 1, c])
    if is_inside(size, r, c + 1):
        houses.append([r, c + 1])
    if is_inside(size, r, c - 1):
        houses.append([r, c - 1])
    return houses


def get_next_position(direction, r, c, steps=1):
    if direction == "right":
        return r, c + steps
    if direction == "left":
        return r, c - steps
    if direction == "up":
        return r - steps, c
    if direction == "down":
        return r + steps, c


def is_inside(size, r, c):
    return 0 <= r < size or 0 <= c < size


presents = int(input())
size = int(input())

matrix = []

santa_row, santa_col = 0, 0
start_good_kids = 0
for row in range(size):
    elements = [x for x in input().split()]
    matrix.append(elements)
    for col in range(size):
        element = elements[col]
        if element == "S":
            santa_row, santa_col = row, col
        elif element == "V":
            start_good_kids += 1

good_kids_count = start_good_kids

while True:
    command = input()
    if command == "Christmas morning":
        break

    next_santa_row, next_santa_col = get_next_position(command, santa_row, santa_col)
    if matrix[next_santa_row][next_santa_col] == "V":
        good_kids_count -= 1
        presents -= 1
    elif matrix[next_santa_row][next_santa_col] == "C":
        houses_in_range = get_houses_in_range(size, next_santa_row, next_santa_col)
        for row, col in houses_in_range:
            if matrix[row][col] == "X":
                presents -= 1
            if matrix[row][col] == "V":
                presents -= 1
                good_kids_count -= 1
            matrix[row][col] = '-'
            if presents == 0:
                break

    matrix[santa_row][santa_col] = '-'
    matrix[next_santa_row][next_santa_col] = 'S'
    santa_row, santa_col = next_santa_row, next_santa_col

    if presents == 0:
        break

if presents == 0 and good_kids_count > 0:
    print("Santa ran out of presents!")

for el in matrix:
    print(' '.join(el))

if good_kids_count == 0:
    print(f"Good job, Santa! {start_good_kids} happy nice kid/s.")
else:
    print(f"No presents for {good_kids_count} nice kid/s.")
