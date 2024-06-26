import sys

n = int(input())
lst = list(map(int, input().split()))
min_val = sys.maxsize

for i in range(n):
    temp = 0
    for j in range(n):
        diff = abs(i - j)
        temp += lst[j] * diff
    min_val = min(min_val, temp)

print(min_val)