n, t = map(int, input().split())
r, c, d = input().split()
r = int(r) - 1
c = int(c) - 1

dr, dc = 0, 0
if d == 'U':
    dr = -1
elif d == 'D':
    dr = 1
elif d == 'R':
    dc = 1
elif d == 'L':
    dc = -1

for _ in range(t):
    if r + dr <= -1 or r + dr >= n:
        dr = -dr
        continue    
    elif c + dc <= -1 or c + dc >= n:
        dc = -dc
        continue
    r += dr
    c += dc
        
r += 1
c += 1
print(r, c)