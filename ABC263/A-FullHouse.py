import collections

num_list = list(map(int, input().split()))
c = collections.Counter(num_list)
values, counts = zip(*c.most_common())

if len(counts) == 2 and counts[0] == 3:
	print("Yes")
else:
	print("No")
