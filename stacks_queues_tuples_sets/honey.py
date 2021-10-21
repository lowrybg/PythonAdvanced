import sys
from io import StringIO
from collections import deque

test_input_one = """20 62 99 35 0 150
120 60 10 1 70 10
+ - + + / * - - /
"""
test_input_two = """30
15 9 5 150 8
* + + * -
"""

# sys.stdin = StringIO(test_input_one)
# sys.stdin = StringIO(test_input_two)

bees = deque([int(x) for x in input().split()])
nectar = [int(x) for x in input().split()]
arithmetic_chars = deque([x for x in input().split()])

arithmetic_dict = {
    '+': lambda a, b: a + b,
    '-': lambda a, b: a - b,
    '*': lambda a, b: a * b,
    '/': lambda a, b: a / b,

}
total_honey = 0
while bees and nectar:
    current_bee = bees[0]
    current_nectar = nectar[-1]
    if current_bee >= current_nectar:
        current_nectar = nectar.pop()
        continue
    current_bee = bees.popleft()
    current_nectar = nectar.pop()
    current_arithm_ch = arithmetic_chars.popleft()

    total_honey += abs(arithmetic_dict[current_arithm_ch](current_bee,current_nectar))
a =5


print(f'Total honey made: {total_honey}')
if bees:
    print(f'Bees left: {", ".join([str(b) for b in bees])}')
if nectar:
    print(f'Nectar left: {", ".join([str(n) for n in nectar])}')