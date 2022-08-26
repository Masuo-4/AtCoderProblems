# 訂正版(動的計画法により計算量O(N)で済む)

n = int(input())
num_list = list(map(int, input().split()))

dp = [0] * (n + 1)
for i in range(2, n + 1):
	dp[i] = dp[num_list[i - 2]] + 1

print(dp)
