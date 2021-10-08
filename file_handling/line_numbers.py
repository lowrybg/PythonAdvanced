
with open("text.txt", "r") as file:
    lines = file.readlines()
    counter = 1
    letters = 0
    punct = 0
    puncs = "[,.!?-\"\']"
    for l in lines:
        for ch in l:
            if ch.isalpha():
                letters += 1
            elif ch in puncs:
                punct += 1

        output = open("output.txt", "a")
        output.write(f'Line {counter}: {l[:-1]} ({letters}) ({punct})\n')
        output.close()

        letters = 0
        punct = 0
        counter += 1
