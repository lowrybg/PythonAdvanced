nums = input().split()

reverse = []
while nums:
    reverse.append(nums.pop())

print(" ".join(reverse))