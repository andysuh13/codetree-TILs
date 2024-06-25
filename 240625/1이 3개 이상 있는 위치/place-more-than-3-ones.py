n = int(input())
maps = []
for _ in range(n):
    maps.append(list(map(int, input().split())))

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

result = 0
for i in range(n):
    for j in range(n):
        cnt = 0
        for k in range(4):
            nr = i + dr[k]
            nc = j + dc[k]
            if nr <= -1 or nr >= n or nc <= -1 or nc >= n:
                continue
            if maps[nr][nc] == 1:
                cnt += 1
        if cnt >= 3:
            result += 1   
print(result)