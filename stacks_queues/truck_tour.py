import sys
from collections import deque
from io import StringIO

test_input_one = """3
1 5
10 3
3 4
"""
my_test = """5
6 6
6 6
6 15
15 5
6 12
"""

# sys.stdin = StringIO(test_input_one)
# sys.stdin = StringIO(my_test)

num = int(input())

deq = deque()

for _ in range(num):
    deq.append(input())

counter = 0
boolean = False
position = 0
petrol = 0
while not counter == len(deq) or boolean:
    split_it = deq[counter]
    nums = [int(x) for x in split_it.split()]
    petrol += nums[0]
    km = nums[1]

    if petrol < km:
        counter = 0
        deq.append(deq.popleft())
        position += 1
        if position == len(deq):
            boolean = True
            break
        petrol = 0
        continue
    else:
        counter += 1
        petrol -= km
if not boolean:
    print(position)
else:
    print("Can't make the tour from any of the positions!")