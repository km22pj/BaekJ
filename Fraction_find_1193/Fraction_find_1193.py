num = int(input())
cnt = 1
i = 1

while True:
    if cnt + i > num:
        break
    cnt += i
    i += 1

if i % 2 == 0:
    left = 1
    right = i
    for k in range(i):
        if cnt == num:
            break
        left += 1
        right -= 1
        cnt += 1

else:
    right = 1
    left = i
    for k in range(i):
        if cnt == num:
            break
        left -= 1
        right += 1
        cnt += 1

print(str(left) + "/" + str(right))