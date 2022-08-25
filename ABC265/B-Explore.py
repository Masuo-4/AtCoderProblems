room_num, bonus_room_num, time = map(int, input().split())
move_cost_lst = list(map(int, input().split()))
bonus_room_dict = dict([tuple(map(int, input().split())) for _ in range(bonus_room_num)])

counter = 1
flag = True
for i in range(room_num - 1):
    counter += 1
    time -= move_cost_lst[i]
    if time <= 0:
        flag = False
        break
    if counter in bonus_room_dict:
        time += bonus_room_dict[counter]

if flag:
	print("Yes")
else:
	print("No")