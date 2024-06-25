N = int(input())

cx, cy = 0, 0
for _ in range(N):
    dir, num = input().split()
    num = int(num)

    if dir == 'W':
        cx -= num
    elif dir == 'S':
        cy -= num
    elif dir == 'N':
        cy += num
    else:
        cx += num
print(cx, cy)