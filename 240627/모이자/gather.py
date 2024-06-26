# n = 5
# arr = [1, 5, 2, 6, 8]
# max_sum = 0

# for i in range(n):
#     arr[i] *= 2
#     sum_diff = 0
#     for j in range(n - 1):
#         sum_diff += abs(arr[j + 1] - arr[j])
#     max_sum = max(max_sum, sum_diff)
#     arr[i] //= 2
# print(max_sum)

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