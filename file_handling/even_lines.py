import re


def replace_punctuation(line):
    return re.sub(r"[,.!?-]", '@', line)


with open("text.txt", "r") as file:
    lines = file.readlines()
    for i in range(len(lines)):
        if i % 2 == 0:
            result = replace_punctuation(lines[i]).split()
            print(" ".join(result[::-1]))