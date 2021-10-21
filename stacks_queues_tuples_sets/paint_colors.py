import sys
from io import StringIO
from collections import deque

test_input_one = """d yel blu e low redd"""
test_input_two = """re ple blu pop e pur d"""

sys.stdin = StringIO(test_input_one)
# sys.stdin = StringIO(test_input_two)


main_colors = ["red", "yellow", "blue"]
secondary_colors = ["orange", "purple", "green"]

substring = deque([x for x in input().split()])

mapper = {
    'orange': ['red', 'yellow'],
    'purple': ['red', 'blue'],
    'green': ['yellow', 'blue'],
}

made_main_colors = []
made_secondary_colors = []
while not len(substring) == 0:
        left = substring.popleft()
        if len(substring) > 1:
            right = substring.pop()
        if left + right in main_colors:
            made_main_colors.append(left + right)
        elif left + right in secondary_colors:
            secondary_colors.append(left + right)
        else:
            if right + left in main_colors:
                made_main_colors.append(left + right)
            elif right + left in secondary_colors:
                secondary_colors.append(left + right)
            else:
                if left and right:
                    left = left[:-1]
                    right = right[:-1]
                if left:
                    substring.insert(len(substring) // 2 ,left)
                if right:
                    substring.insert(len(substring) // 2, right)

