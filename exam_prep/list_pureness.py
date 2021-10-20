from collections import deque


def best_list_pureness(*args):
    my_deq = deque(args[0])
    k = args[1]
    my_dict = {}
    for _ in range(k):
        temp_res = 0

        for n in range(len(my_deq)):
            temp_res += my_deq[n] * n
            if n == len(my_deq) - 1:
                my_deq.appendleft(my_deq.pop())
                my_dict.update({temp_res: k-1})
    maxi = max(my_dict.keys())
    for k, v in my_dict.items():
        if k == maxi:
            return f"Best pureness {k} after {v} rotations"


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
