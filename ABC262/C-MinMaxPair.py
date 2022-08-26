import math

n = int(input())
num_lst = list(map(int, input().split()))

reverse_count = 0
same_count = 0
for i, num in enumerate(num_lst):
    if num == i + 1:
        same_count += 1
    elif num_lst[num - 1] == i + 1:
        reverse_count += 1

print(math.comb(same_count, 2) + int(reverse_count / 2))