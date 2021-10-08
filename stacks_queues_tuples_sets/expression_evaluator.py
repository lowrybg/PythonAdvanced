import sys
from collections import deque
from io import StringIO
import  math

test_input_one = """6 3 - 2 1 * 5 /"""
test_input_two = """2 2 - 1 *"""

sys.stdin = StringIO(test_input_one)
# sys.stdin = StringIO(test_input_two)

line = deque(input().split())
operations = []
result = ''
for chars in line:
    if chars not in '*+-/':
        operations.append(int(chars))
    else:
        if chars == '-':
            result = [(x-x) for x in operations]