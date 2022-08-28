import numpy as np

# r行c列目をスタート地点とし、そこからd方向にnum回移動して通った値を整数で出力
def move(num, r, c, d):
    lst = []
    for _ in range(num):
        lst.append(maze[r][c])
        if "U" in d:
            if r >= 1:
                r -= 1
            else:
                r = num - 1
        if "D" in d:
            if r < num - 1:
                r += 1
            else:
                r = 0
        if "R" in d:
            if c < num - 1:
                c += 1
            else:
                c = 0
        if "L" in d:
            if c >= 1:
                c -= 1
            else:
                c = num - 1

    return int("".join(map(str, lst)))

# 配列を作成
n = int(input())
maze = []
for i in range(n):
	maze.append(list(map(int, input())))
maze = np.array(maze)

# 最大値の行と列の番号を記録
max_arg_lst = [i for i, x in enumerate(maze.ravel()) if x == max(maze.ravel())]
max_rc_lst = []
for max_arg in max_arg_lst:
    max_row = max_arg // n
    max_col = max_arg % n
    max_rc_lst.append([max_row, max_col])

# 最大値スタートで、八方向の総当たり
ans_lst = []
move_lst = ["U", "D", "L", "R", "UL", "UR", "DL", "DR"]
for direction in move_lst:
    for rc in max_rc_lst:
        ans_lst.append(move(n, rc[0], rc[1], direction))

print(max(ans_lst))
