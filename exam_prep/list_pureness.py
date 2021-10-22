from collections import deque


def best_list_pureness(*args):
    my_deq = deque(args[0])
    k = args[1]
    result = 0
    rotations = 0
    for _ in range(k+1):
        temp_res = 0

        for n in range(len(my_deq)):
            temp_res += my_deq[n] * n
            if n == len(my_deq) - 1:
                my_deq.appendleft(my_deq.pop())
            if result < temp_res:
                result = temp_res
                rotations += 1
    return f"Best pureness {k} after {rotations} rotations"


# test = ([4, 3, 2, 6], 4)
# result = best_list_pureness(*test)
# print(result)
#
# test = ([7, 9, 2, 5, 3, 4], 3)
# result = best_list_pureness(*test)
# print(result)

test = ([1, 2, 3, 4, 5], 10)
result = best_list_pureness(*test)
print(result)
