import sys
from io import StringIO

test_input_one = """4
Pesho
Stefan
Stamat
Gosho
"""
test_input_two = """6
Preslav
Gosho
Ivan
Stamat
Pesho
Stefan
"""

# sys.stdin = StringIO(test_input_one)
# sys.stdin = StringIO(test_input_two)

n = int(input())
even = set()
odd = set()

for i in range(1, n + 1):
    line = input()
    temp = []
    for ch in line:
        temp.append(ord(ch))
    if (sum(temp) // i) % 2 == 0:
        even.add(sum(temp) // i)
    else:
        odd.add(sum(temp) // i)


if sum(even) == sum(odd):
    print(", ".join([str(x) for x in odd.union(even)]))
elif sum(even) < sum(odd):
    print(", ".join([str(x) for x in (odd.difference(even))]))
else:
    print(", ".join([str(x) for x in odd.symmetric_difference(even)]))