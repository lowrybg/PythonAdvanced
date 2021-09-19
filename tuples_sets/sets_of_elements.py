lines = input().split()

set_one_len, set_two_len = int(lines[0]), int(lines[1])

set_one = set()
set_two = set()


def add_el_to_set(for_range: int):
    my_set = set()
    for _ in range(for_range):
        line = input()
        my_set.add(line)
    return my_set


set_one = add_el_to_set(set_one_len)
set_two = add_el_to_set(set_two_len)
inter = set_one.intersection(set_two)

print("\n".join([x for x in inter]))


