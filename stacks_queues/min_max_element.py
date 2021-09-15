lines = int(input())

stack = []
for _ in range(lines):
    command_line = input()
    if command_line.startswith('1'):
        command_line = command_line.split()
        stack.append(int(command_line[1]))
    elif command_line.startswith('2') and len(stack) > 0:
        stack.pop()
    elif command_line.startswith('3') and len(stack) > 0:
        print(max(stack))
    elif command_line.startswith('4') and len(stack) > 0:
        print(min(stack))


result = []
for _ in range(len(stack)):
    result.append(str(stack.pop()))
print(", ".join(result))

