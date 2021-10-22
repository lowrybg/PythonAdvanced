import sys
from io import StringIO

test_input_one = """3, 1, 10, 1, 2
0
"""
test_input_two = """"""

# sys.stdin = StringIO(test_input_one)
# sys.stdin = StringIO(test_input_two)

numbers = ([int(x) for x in input().split(', ')])
index = int(input())


def solve (nums, index):
    my_tuple = [(i,n) for n,i in enumerate(nums)]
    result = 0
    for num, ind in sorted(my_tuple, key=lambda x:x[0]):
        result += num
        if ind == index:
            break
    return result


print(solve(numbers,index))