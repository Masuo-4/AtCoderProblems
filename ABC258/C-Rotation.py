n, q = list(map(int, input().split()))
s = input()

query_lst = []
for i in range(q):
    query_lst.append(list(map(int, input().split())))

count = 0
for t, x in query_lst:
    if t == 1:
        count += x
    else:
        print(s[(x - count - 1) % n])
