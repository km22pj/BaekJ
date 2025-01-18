input_num, system = input().strip().split()

num_list = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9}
for i in range(65, 91):
    num_list[chr(i)] = i - 55
sum_ = 0
num_len = len(input_num)
for i in range(num_len):
    sum_ += num_list[input_num[i]] * (int(system) ** (num_len-i-1))
print(sum_)