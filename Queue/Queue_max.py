
max_val = 0
max_index = [0, 0]
for i in range(1, 10):
    que1 = list(map(int, input().strip().split()))
    if max_val <= max(que1):
        max_val = max(que1)
        max_index[0] = i
    for j in range(1, 10):
        if que1[j-1] == max_val:
            max_index[1] = j

print(max_val)
print(*max_index)
