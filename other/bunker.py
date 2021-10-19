import sys
from io import StringIO

test_input_one = """food, water, materials, metal
5
food - pizza - quantity:10;quality:5
water - mineral - quantity:5;quality:10
materials - wood - quantity:2;quality:5
metal - copper - quantity:3;quality:10
food - burgers - quantity:5;quality:2
"""
# test_input_two = """"""

sys.stdin = StringIO(test_input_one)
# sys.stdin = StringIO(test_input_two)

categories = input().split(', ')
lines_num = int(input())


category_dict = {}
count_items = 0
count_quality = 0
for row in range(lines_num):
    category, element, *others = input().split(' - ')

    quantity, quality = [[y for y in x.split(':')]for x in others[0].split(';')]
    count_items += int(quantity[1])
    count_quality += int(quality[1])
    # todo if there is unique elements
    if not category in category_dict:
        category_dict[category] = []
        category_dict[category].append(element)
        # category_dict[category][0]
        # print(category_dict[category][0])
    else:
        category_dict[category].append(element)

print(f'Count of items: {count_items}')
print(f'Average quality: {count_quality/len(category_dict):.2f}')
print(*[f'{key} -> {", ".join(v)}'for key,v in category_dict.items()], sep='\n')