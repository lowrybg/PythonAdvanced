command = input()
nums = list(map(int, input().split()))

if command == 'Odd':
    print(*[sum([x for x in nums if x%2!=0])*len(nums)])
elif command == 'Even':
    print(*[sum([x for x in nums if x % 2 == 0]) * len(nums)])