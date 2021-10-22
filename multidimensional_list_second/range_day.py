def get_next_position(direction, r, c, steps):
    if direction == "right":
        return r, c + steps
    if direction == "left":
        return r, c - steps
    if direction == "up":
        return r - steps, c
    if direction == "down":
        return r + steps, c

size = 5

matrix = []

player_row, player_col = 0, 0
targets_count = 0
for row in range(size):
    elements = [x for x in input().split()]
    matrix.append(elements)
    for col in range(size):
        element = elements[col]
        if element == "A":
            player_row, player_col = row, col
        elif element == "x":
            targets_count += 1


def is_inside(r, c, size):
    return 0 <= r < size and 0 <= c < size


n = int(input())
targets_hit = []

for _ in range(n):
    args = input().split()
    command = args[0]
    direction = args[1]

    if command == "move":
        steps = int(args[2])
        next_player_row, next_player_col = get_next_position(direction, player_row, player_col, steps)

        if not is_inside(next_player_row, next_player_col, size):
            continue
        if matrix[next_player_row][next_player_col] != '.':
            continue
        matrix[player_row][player_col] = '.'
        matrix[next_player_row][next_player_col] = 'A'
        player_row, player_col = next_player_row, next_player_col
    else:
        bullet_row, bullet_col = get_next_position(direction, player_row, player_col, 1)
        while True:
            if not is_inside(bullet_row, bullet_col, size):
                break

            if matrix[bullet_row][bullet_col] == "x":
                targets_hit.append([bullet_row, bullet_col])
                matrix[bullet_row][bullet_row] = '.'
                break

            bullet_row, bullet_col = get_next_position(direction, bullet_row, bullet_col, 1)
        if len(targets_hit) == targets_count:
            break

if len(targets_hit) == targets_count:
    print(f"Training completed! All {targets_count} targets hit.")
else:
    print(f"Training not completed! {targets_count - len(targets_hit)} targets left.")

for target in targets_hit:
    print(target)
