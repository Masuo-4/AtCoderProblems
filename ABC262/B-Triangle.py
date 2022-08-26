import itertools
vertex, edge_num = map(int, input().split())
adj = [[False] * vertex for _ in range(vertex)]

for i in range(edge_num):
	u, v = map(int, input().split())
	adj[u - 1][v - 1] = True
	adj[v - 1][u - 1] = True

count = 0
lst = [i for i in range(1, vertex + 1)]
for i, j, k in itertools.combinations(lst, 3):
	i -= 1
	j -= 1
	k -= 1
	if adj[i][j] and adj[i][k] and adj[k][j]:
    	 count += 1

print(count)
