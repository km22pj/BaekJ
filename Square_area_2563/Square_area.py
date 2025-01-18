squ_num = int(input())
sum_are = 0
area = [[0]*100 for _ in range(100)]

for _ in range(squ_num):
    x, y = map(int, input().strip().split())
    for i in range(x, x+10):
        for j in range(y, y+10):
            area[i][j] = 1

for i in range(100):
    sum_are += area[i].count(1)
print(sum_are)
