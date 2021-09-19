import sys
from io import StringIO

test_input_one = """SoftUni rocks"""
test_input_two = """WhWy do you like Python?"""

# sys.stdin = StringIO(test_input_one)
# sys.stdin = StringIO(test_input_two)

text = input()

my_dict = {}

for ch in text:
    if not ch in my_dict:
        my_dict[ch] = 1
    else:
        my_dict[ch] += 1

my_dict = sorted(my_dict.items(), key=lambda x: x[0])

for k, v in my_dict:
    print(f'{k}: {v} time/s')
