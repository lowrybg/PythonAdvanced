import sys
from io import StringIO

test_input_one = """3
0,3-1,2
2,10-3,5
6,15-3,10
"""
test_input_two = """5
0,10-2,5
3,8-1,7
1,8-2,4
4,7-2,5
1,10-2,11
"""

# sys.stdin = StringIO(test_input_one)
# sys.stdin = StringIO(test_input_two)

n = int(input())
set_one = set()
set_two = set()
longest_inter = set()

for _ in range(n):
    line = input().split('-')
    first_first, first_second = [int(x) for x in line[0].split(',')]
    second_first, second_sec = [int(x) for x in line[1].split(',')]

    set_one = set()
    set_two = set()
    for s in range(first_first,first_second + 1):
        set_one.add(s)
    for t in range(second_first, second_sec + 1):
        set_two.add(t)
    inter = set_one.intersection(set_two)
    if len(inter) > len(longest_inter):
        longest_inter = inter

print(f'Longest intersection is {list(longest_inter)} with length {len(longest_inter)}')

