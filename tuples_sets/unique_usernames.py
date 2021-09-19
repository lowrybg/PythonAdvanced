import sys
from io import StringIO

test_input_one = """6
George
George
George
Peter
George
NiceGuy1234"""
test_input_two = """10
Peter
Maria
Peter
George
Steve
Maria
Alex
Peter
Steve
George"""

# sys.stdin = StringIO(test_input_one)
# sys.stdin = StringIO(test_input_two)

num = int(input())

names = set()
for el in range(num):
    line = input()
    names.add(line)

for el in names:
    print(el)