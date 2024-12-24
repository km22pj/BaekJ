num = int(input())
cnt = 0

while num > 0:
    char_list = []
    word = input()
    num -= 1
    for index, ch in enumerate(word):
        if ch not in char_list:
            char_list.append(ch)
        else:
            if word[index-1] == ch:
                pass
            else:
                break
        if index+1 == len(word):
            cnt += 1
print(cnt)