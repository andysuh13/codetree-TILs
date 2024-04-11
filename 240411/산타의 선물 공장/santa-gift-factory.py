from collections import deque
import sys

q = int(input()) # 명령의 수

lst = list(map(int, sys.stdin.readline().rstrip().split()))

n = lst[1] # 선물의 수
m = lst[2] # 벨트의 수

id_lst = lst[3 : n + 3]
w_lst = lst[n+3 : ]

belt_lst = []
belt_broken_check = []
for i in range(m):
    belt_lst.append(deque())
    belt_broken_check.append(True)

for (i, (id, w)) in enumerate(zip(id_lst, w_lst)):
    belt_num = i // (n // m)
    belt_lst[belt_num].append((id, w))

for _ in range(q - 1):
    temp = list(map(int, input().split()))
    cmd_num = temp[0]
    target = temp[1]
    result = 0

    # 물건 하차 : 200 w_max : 하차된 상자 무게의 총합을 출력해야 함.
    # 1번 벨트부터 m번 벨트까지 순서대로 벨트를 보며 각 벨트의 맨 앞에 있는 선물 중 해당 선물의 무게가 w_max이하라면 하차 진행.
    if cmd_num == 200:
        for belt in belt_lst:
            if belt[0][1] <= target:
                result += belt.popleft()[1]
            else:
                pass
        print(result)
        continue


    # 물건 제거 : 300 r_id : 그러한 상자가 있는 경우 r_id 값을, 없다면 -1을 출력해야 함.
    # r_id : 제거하기를 원하는 물건의 고유 번호
    # r_id를 id로 하는 상자가 있다면 제거, 없다면 아무것도 안 함.
    elif cmd_num == 300:
        r_id = target
        check = True
        for belt in belt_lst:
            for data in belt:
                if data[0] == r_id:
                    check = False
                    print(r_id)
                    break
                else:
                    pass
            if check == False:
                belt.remove(data)
                break
            else:
                pass
        if check == True:
            print(-1)
        continue    

    # 물건 확인 : 400 f_id : 해당하는 상자가 있다면 상자가 있는 벨트의 번호를 출력, 없다면 -1 출력
    # 해당하는 상자부터 그 뒤에 상자들 모두 벨트의 맨 앞으로 끌고 와야 함.
    elif cmd_num == 400:
        f_id = target
        check = True
        for belt in belt_lst:
            for idx, data in enumerate(belt):
                if data[0] != f_id:
                    pass
                else:
                    check = False
                    print(belt_lst.index(belt) + 1)
                    for _ in range(idx):
                        belt.append(belt.popleft())
                    break
            if check == False:
                break
            else:
                pass
        if check == True:
            print(-1)
        continue

    # 벨트 고장 : 500 b_num : b_num 벨트가 이미 망가져 있었다면 -1 출력, 아니면 b_num 출력 
    elif cmd_num == 500:
        b_num = target
        b_idx = b_num - 1 
        if belt_broken_check[b_idx] == False:
            print(-1)
        else:
            belt_broken_check[b_idx] = False
            for k in range(m - 1):
                current = b_idx + (k + 1)
                if current >= m:
                    current %= m
                if belt_broken_check[current] == True:
                    break
            dst_belt_idx = current
            while belt_lst[b_idx]:
                belt_lst[dst_belt_idx].append(belt_lst[b_idx].popleft())
            print(b_num)
        continue