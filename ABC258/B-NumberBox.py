import numpy as np
n = int(input())
maze = []
for i in range(n):
	maze.append(list(map(int, input().split())))

# 地図作成
arr = np.array(maze)
arr = np.hstack([arr] * n)
arr = np.vstack([arr] * n)

max_row = n + maze.argmax() // n
max_col = n + maze.argmax() % n

arr[max_row - 1: max_row + 1, max_col - 1: max_col + 1]