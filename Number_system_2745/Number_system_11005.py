input_num, system = map(int, input().strip().split())

num_list = {0: "0", 1: "1", 2: "2", 3: "3", 4: "4", 5: "5", 6: "6", 7: "7", 8: "8", 9: "9"}
for i in range(65, 91):
    num_list[i-55] = chr(i)
ans = ""

while (input_num // system) != 0:
    ch = num_list[input_num % system]
    input_num = input_num // system
    ans = ch + ans

ans = num_list[input_num % system] + ans
print(ans)