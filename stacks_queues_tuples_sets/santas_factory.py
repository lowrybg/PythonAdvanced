import sys
from io import StringIO
from collections import deque

test_input_one = """10 -5 20 15 -30 10
40 60 10 4 10 0
"""
test_input_two = """30 5 15 60 0 30
-15 10 5 -15 25
"""

# sys.stdin = StringIO(test_input_one)
# sys.stdin = StringIO(test_input_two)

materials = [int(x) for x in input().split()]
magic_values = deque([int(x) for x in input().split()])


mapper = {
    150: "Doll",
    250: "Wooden train",
    300: "Teddy bear",
    400: "Bicycle",
}

crafted_presents = {}
while materials and magic_values:
    magic_level = materials[-1] * magic_values[0]
    try:
        if magic_level in mapper:
            toy = mapper[magic_level]
            if toy not in crafted_presents:
                crafted_presents.update({toy:1})

            else:
                crafted_presents[toy] += 1
            materials.pop()
            magic_values.popleft()
            continue
        if magic_level < 0:
            to_append_mat = materials[-1] + magic_values[0]
            materials.pop()
            magic_values.popleft()
            materials.append(to_append_mat)
        if magic_level > 0 and magic_level not in mapper:
            magic_values.popleft()
            materials[-1] += 15
        if materials[-1] == 0:
            materials.pop()
        if magic_values[0] == 0:
            magic_values.popleft()
    except IndexError:
        pass

if ('Teddy bear' and 'Bicycle') in crafted_presents or ('Doll' and 'Wooden train') in crafted_presents:
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")
print(f"Materials left: {', '.join([str(m) for m in materials[::-1]])}")
for k, v in sorted(crafted_presents.items()):
    print(f'{k}: {v}')