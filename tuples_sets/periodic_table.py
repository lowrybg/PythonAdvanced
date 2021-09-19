import sys
from io import StringIO

test_input_one = """4
Ce O
Mo O Ce
Ee
Mo
"""
test_input_two = """3
Ge Ch O Ne
Nb Mo Tc
O Ne
"""

# sys.stdin = StringIO(test_input_one)
# sys.stdin = StringIO(test_input_two)

n = int(input())

my_set = set()
for el in range(n):
    line = input().split()
    for x in line:
        my_set.add(x)


print("\n".join(my_set))