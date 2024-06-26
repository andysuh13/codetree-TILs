n = int(input())
lst = list(map(int, input().split()))

cnt = 0

for i in range(n):
    result = []
    result.append(lst[i])
    for j in range(i + 1, n):
        if (result[-1] <= lst[j]) & (len(result) < 3):
            result.append(lst[j])
        if len(result) == 3:
            cnt += 1
            break
print(cnt)