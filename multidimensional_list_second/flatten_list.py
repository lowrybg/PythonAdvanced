import sys
from io import StringIO

test_input_one = """1 2 3 |4 5 6 |  7  88"""
test_input_two = """7 | 4  5|1 0| 2 5 |3"""

# sys.stdin = StringIO(test_input_one)
# sys.stdin = StringIO(test_input_two)

line = input().split('|')

result = []

for el in range(len(line)-1, -1, -1):
    result.extend(line[el].split())

print(*result)

