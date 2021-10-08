import sys
from io import StringIO

test_input_one = """1 2 3 4 5
1 2 3
3
Add First 5 6
Remove Second 8 9 11
Check Subset
"""
test_input_two = """5 4 2 9 9 5 4
1 1 1 5 6 5
4
Add First 5 6 9 3
Add Second 1 2 3 3 3
Check Subset
Remove Second 1 2 3 4 5
"""

# sys.stdin = StringIO(test_input_one)
# sys.stdin = StringIO(test_input_two)


def ch_to_set(elements: list):
    my_set = set()
    for el in elements:
        my_set.add(el)
    return my_set


first_sequence = input().split()
second_sequence = input().split()

first_set = ch_to_set(first_sequence)
second_set = ch_to_set(second_sequence)

n = int(input())

for _ in range(n):
    command, subcommand, *numbers = input().split()
    if command == 'Add':
        if subcommand == 'First':
            for i in numbers:
                first_set.add(i)
        elif subcommand == 'Second':
            for s in numbers:
                second_set.add(s)
    elif command == 'Remove':
        if subcommand == 'First':
            for first in numbers:
                if first in first_set:
                    first_set.remove(first)
        elif subcommand == 'Second':
            for sec in numbers:
                if sec in second_set:
                    second_set.remove(sec)
    elif command == 'Check':
        if subcommand == 'Subset':
            if first_set.issubset(second_set) or second_set.issubset(first_set):
                print("True")
            else:
                print('False')


first_set = sorted(first_set)
second_set = sorted(second_set)

print(", ".join(first_set))
print(", ".join(second_set))
