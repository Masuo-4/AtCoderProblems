import itertools

# 入力
vertex, edge_num = map(int, input().split())
pair = []
for i in range(edge_num):
	pair.append(list(map(int, input().split())))

# 頂点の組み合わせのリスト作成
edge_lst = [[] for _ in range(vertex)]
for i in pair:
	edge_lst[i[0] - 1].append(i[1])
	edge_lst[i[1] - 1].append(i[0])
for lst in edge_lst:
    lst.sort()

# 頂点の組み合わせを全部調べる
count = 0
num = [i for i in range(1, vertex + 1)]
for v in itertools.combinations(num, 3):
    if v[1] in edge_lst[v[0] - 1] and v[2] in edge_lst[v[0] - 1]:
        if v[2] in edge_lst[v[1] - 1]:
            count += 1
            
print(count)
