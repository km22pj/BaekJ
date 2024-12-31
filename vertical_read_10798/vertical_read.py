words = []
for _ in range(5):
    word = input()
    words.append(word)

for i in range(15):
    for j in range(5):
        try:
            print(words[j][i], end='')
        except IndexError:
            pass