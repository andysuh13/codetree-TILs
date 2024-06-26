data = input()

cnt = 0

for i in range(len(data) - 1):
    for j in range(i + 1, len(data)):
        if (data[i] == '(') & (data[j] == ')'):
            cnt += 1
print(cnt)