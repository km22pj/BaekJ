words = [input() for _ in range(5)]
max_len = max([len(s) for s in words])

for i in range(max_len):
    for j in range(5):
        try:
            print(words[j][i], end='')
        except IndexError:
            pass