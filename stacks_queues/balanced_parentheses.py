import sys
from collections import deque
from io import StringIO

test_input_one = """{[()]}"""
test_input_two = """()[()]"""

# sys.stdin = StringIO(test_input_one)
sys.stdin = StringIO(test_input_two)

line = input()

deq = deque()
for el in line:
    if el in '{[(':
        deq.append(el)
    elif deq:
        if el == ')' and deq[-1] == '(':
            deq.pop()
        elif el == ']' and deq[-1] == '[':
            deq.pop()
        elif el == '}' and deq[-1] == '{':
            deq.pop()
        else:
            break

if not deq:
    print('YES')
else:
    print('NO')

# TODO it reach only 75% on judge
