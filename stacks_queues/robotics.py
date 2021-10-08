import sys
from collections import deque
from io import StringIO
from datetime import timedelta
from datetime import datetime

test_input_one = """ROB-15;SS2-10;NX8000-3
8:00:00
detail
glass
wood
apple
End
"""
test_input_two = """ROB-8
7:59:59
detail
glass
wood
sock
End
"""

sys.stdin = StringIO(test_input_one)
# sys.stdin = StringIO(test_input_two)

robots = input().split(';')
my_dict = {}

for el in robots:
    rob_name, processing_time = el.split('-')
    my_dict[rob_name] = int(processing_time)

time = input().split(':')
line = input()
deq = deque()
while not line == 'End':
    deq.append(line)
    line = input()

t = datetime(year=None, hour=time[0], minute=time[1], second=time[2])

my_list = list(my_dict)
counter = 0

while deq:
    t += timedelta(seconds=1)
    print(f'{my_list[counter]} - {deq.popleft()} [{t}]')
    counter += 1
    if counter == len(my_list):
        counter = 0

# todo
