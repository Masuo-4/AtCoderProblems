n = int(input())
num_list = list(map(int, input().split()))

ans = 0
while n != 1:
	n = num_list[n - 2]
	ans += 1

print(ans)