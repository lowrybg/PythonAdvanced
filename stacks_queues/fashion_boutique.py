import sys
from io import StringIO

test_input_one = """5 4 8 6 3 8 7 7 9
16
"""
test_input_two = """1 7 8 2 5 4 7 8 9 6 3 2 5 4 6
20

"""

# sys.stdin = StringIO(test_input_one)
# sys.stdin = StringIO(test_input_two)

boxes = input().split()
rack_capacity = int(input())
temp_rack = rack_capacity
stack = []
for el in boxes:
    stack.append(int(el))
counter = 1
while stack:
    if not temp_rack >= stack[-1]:
        temp_rack = rack_capacity
        counter += 1

    temp_rack -= stack.pop()

print(counter)