r, c = map(int, input().split())
maps = []
for _ in range(r):
    maps.append(input().split())

cnt = 0
for i in range(r):
    for j in range(c):
        for k in range(i + 1, r - 1):
            for l in range(j + 1, c - 1):
                if (maps[0][0] != maps[i][j]) & (maps[i][j] != maps[k][l]) & (maps[k][l] != maps[r - 1][c - 1]):
                    cnt += 1

print(cnt)