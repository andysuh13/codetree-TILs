n = int(input())
maps = []
for _ in range(n):
    maps.append(list(map(int, input().split())))

max_val = 0
for i in range(n):
    for j in range(n - 2):
        cnt = maps[i][j] + maps[i][j + 1] + maps[i][j + 2]
        max_val = max(max_val, cnt)
print(max_val)