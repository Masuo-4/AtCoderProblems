def sum_pair(n):
    pair_lst = []
    for i in range(1, n):
        pair_lst.append([i, n - i])
    return pair_lst


h1, h2, h3, w1, w2, w3 = list(map(int, input().split()))
count = 0

for i in range(1, min(h1, w1) - 1):
    for pair1 in sum_pair(h1 - i):
        new_w2, new_w3 = w2 - pair1[0], w3 - pair1[1]
        for pair2 in sum_pair(w1 - i):
            new_h2, new_h3 = h2 - pair2[0], h3 - pair2[1]
            for n in range(1, min(new_w2, new_h2)):
                if new_h2 + new_h3 != new_w2 + new_w3:
                    continue
                else:
                    k = new_h3 - new_w2 + n
                    if k > 0:
                        count += 1
print(count)
