num = int(input())
cnt = 0

while num > 0:
    char_list = []
    word = input()
    num -= 1
    for index, ch in enumerate(word):
        if word.count(ch) == 1:
            pass
        else:
            if ch in char_list:
                if word[index-1] == ch:
                    pass
                else:
                    break
            else:
                char_list.append(ch)
        if index + 1 == len(word):
            cnt += 1
print(cnt)
