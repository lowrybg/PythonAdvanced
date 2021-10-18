import sys
from io import StringIO

test_input_one = """1 2 -3 -4 65 -98 12 57 -84"""
test_input_two = """1 2 3"""

# sys.stdin = StringIO(test_input_one)
# sys.stdin = StringIO(test_input_two)

nums = list(map(int, input().split()))


def solve(numbers):
    positive = sum([int(x)for x in numbers if x > 0])
    negative = sum([int(x)for x in numbers if x < 0])
    print(negative)
    print(positive)
    if abs(positive) < abs(negative):
        print('The negatives are stronger than the positives')
    else:
        print('The positives are stronger than the negatives')



solve(nums)
