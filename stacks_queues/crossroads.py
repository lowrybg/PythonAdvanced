import sys
from collections import deque
from io import StringIO

test_input_one = """10
5
Mercedes
green
Mercedes
BMW
Skoda
green
END
"""
test_input_two = """9
3
Mercedes
Hummer
green
Hummer
Mercedes
green
END
"""

# sys.stdin = StringIO(test_input_one)
# sys.stdin = StringIO(test_input_two)

green = int(input())
free = int(input())

line = input()
cars = deque()
counter = 0
while not line == 'END':
    if not line == 'green':
        cars.append(line)
    else:
        allowed_green = green
        while not allowed_green <= 0 and len(cars) > 0:
            left_green = allowed_green + free
            car_len = len(cars[0])
            if left_green <= car_len:
                print('A crash happened!')
                print(f'{cars[0]} was hit at {cars[0][left_green]}.')
                exit(0)
            elif allowed_green + free >= car_len:
                counter += 1
                cars.popleft()
                allowed_green -= car_len
    line = input()

print('Everyone is safe.')
print(f'{counter} total cars passed the crossroads.')

# todo 71%
