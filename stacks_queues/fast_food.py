import sys
from collections import deque
from io import StringIO

test_input_one = """348
20 54 30 16 7 9
"""
test_input_two = """499
57 45 62 70 33 90 88 76 100 50
"""

# sys.stdin = StringIO(test_input_one)
# sys.stdin = StringIO(test_input_two)

qnty = int(input())
orders = input().split()

dequeue = deque()

for el in orders:
    dequeue.append(int(el))

print(max(dequeue))

while qnty >= 0 and dequeue:
    if not qnty >= dequeue[0]:
        break
    qnty -= dequeue.popleft()

if not dequeue:
    print('Orders complete')
else:
    print(f'Orders left: {" ".join([str(x) for x in dequeue])}')





