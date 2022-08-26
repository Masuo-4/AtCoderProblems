import itertools

length, m = map(int, input().split())

num_lst = [i for i in range(1, m + 1)]
ans_lst = []

for v in itertools.combinations(num_lst, length):
    ans_lst.append(v)

for lst in ans_lst:
    for i in lst:
        print(i, end=" ")
    print()
        