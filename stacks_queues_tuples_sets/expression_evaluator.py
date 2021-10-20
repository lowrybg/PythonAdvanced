import sys
from collections import deque
from io import StringIO
import math

test_input_one = """6 3 - 2 1 * 5 /"""
test_input_two = """2 2 - 1 *"""

# sys.stdin = StringIO(test_input_one)
# sys.stdin = StringIO(test_input_two)

line = input().split()

operations = {
    '+': lambda a, b: a + b,
    '-': lambda a, b: a - b,
    '*': lambda a, b: a * b,
    '/': lambda a, b: a // b,
}
my_deq = deque()

for el in line:
    if el in operations:
        result = my_deq.popleft()
        while my_deq:
            number = my_deq.popleft()
            result = operations[el](result, number)
        my_deq.append(result)
    else:
        my_deq.append(int(el))


print(my_deq.popleft())