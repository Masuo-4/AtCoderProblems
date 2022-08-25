room_num, bonus_room_num, time = map(int, input().split())
move_cost_lst = list(map(int, input().split()))
bonus = [0] * room_num

for _ in range(bonus_room_num):
    i, bonus_time = map(int, input().split())
    bonus[i - 1] = bonus_time


flag = True
for i in range(room_num - 1):
    if time <= move_cost_lst[i]:
        flag = False
        break
    time -= move_cost_lst[i]
    time += bonus[i + 1]
    

if flag:
    print("Yes")
else:
    print("No")