import sys
from collections import deque
from io import StringIO

test_input_one = """20, 24, -5, 17, 22, 60, 26
26, 60, 22, 17, 24, 10, 55
"""
test_input_two = """-10, -2, -30, 10
-5
"""

# sys.stdin = StringIO(test_input_one)
# sys.stdin = StringIO(test_input_two)

chocolates = deque(map(int, input().split(', ')))
milk = deque(map(int, input().split(', ')))
milkshakes = 0
while True:
    if chocolates and milk:
        if chocolates[-1] <= 0:
            chocolates.pop()
        elif milk[0] <= 0:
            milk.popleft()
        if milkshakes == 5 or len(chocolates) <= 0 or len(milk) <= 0:
            break
        if chocolates[-1] == milk[0]:
            chocolates.pop()
            milk.popleft()
            milkshakes += 1
        else:
            milk.append(milk.popleft())
            chocolates[-1] -= 5
    else:
        break
if milkshakes == 5:
    print('Great! You made all the chocolate milkshakes needed!')
else:
    print('Not enough milkshakes.')
if chocolates:
    print(f'Chocolate: {", ".join([str(el) for el in chocolates])}')
else:print(f'Chocolate: empty')
if milk:
    print(f'Milk: {", ".join([str(el) for el in milk])}')
else:
    print(f'Milk: empty')