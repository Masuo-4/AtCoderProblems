row_num, col_num = map(int, input().split())
maze = []
for i in range(row_num):
    maze.append(list(input().split()[0]))

position_x = 0
position_y = 0

while True:
    if maze[position_y][position_x] == 0:
        print(-1)
        exit()

    elif maze[position_y][position_x] == "U":
        if position_y == 0:
            break
        else:
            maze[position_y][position_x] = 0
            position_y -= 1

    elif maze[position_y][position_x] == "D":
        if position_y == row_num - 1:
            break
        else:
            maze[position_y][position_x] = 0
            position_y += 1

    elif maze[position_y][position_x] == "R":
        if position_x == col_num - 1:
            break
        else:
            maze[position_y][position_x] = 0
            position_x += 1

    elif maze[position_y][position_x] == "L":
        if position_x == 0:
            break
        else:
            maze[position_y][position_x] = 0
            position_x -= 1

print(position_y + 1, position_x + 1)
