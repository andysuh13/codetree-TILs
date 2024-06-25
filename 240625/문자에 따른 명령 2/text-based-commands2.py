com = input()

x, y = 0, 0
dir_lst = ['N', 'E', 'S', 'W']
dir_num = 0

for temp in com:
    if temp == 'L':
        dir_num -= 1
        if dir_num < 0:
            dir_num = 3
    elif temp == 'R':
        dir_num += 1
        if dir_num > 3:
            dir_num = 0
    elif temp == 'F':
        if dir_lst[dir_num] == 'N':
            y += 1
        elif dir_lst[dir_num] == 'E':
            x += 1
        elif dir_lst[dir_num] == 'S':
            y -= 1
        elif dir_lst[dir_num] == 'W':
            x -= 1

print(x, y)