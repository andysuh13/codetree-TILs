# class Node:
#     def __init__(self, data=None):
#         self.data = data
#         self.left = None
#         self.right = None
#         self.power = None
# root = Node(0)

n, q = map(int, input().split()) # 채팅방의 수, 명령의 수

for _ in range(q):
    lst = list(map(int, input().split()))

    # 사내 메신저 준비
    if lst[0] == 100: 
        parents_lst = [None] + lst[1:n+1]
        authority_lst = [None] + lst[n+1:]
        switch_lst = [None] + [True] * n

    # 알림망 설정 ON / OFF : 200 c
    elif lst[0] == 200:
        c = lst[1]
        if switch_lst[c-1] == True:
            switch_lst[c-1] = False
        else:
            switch_lst[c-1] = True

    # 권한 세기 변경 : 300 c power
    elif lst[0] == 300:
        c = lst[1]
        power = lst[2]
        authority_lst[c-1] = power

    # 부모 채팅방 교환 : 400 c1 c2 
    elif lst[0] == 400:
        c1 = lst[1]
        c2 = lst[2]
        parents_lst[c1 - 1], parents_lst[c2 - 1] = parents_lst[c2 - 1], parents_lst[c1 - 1]

    # 알림을 받을 수 있는 채팅방 수 조회 : 500 c   
    # c번 채팅방까지 알림이 도달할 수 있는 서로 다른 채팅방의 수 
    elif lst[0] == 500:
        c = lst[1]
        cnt = 0
        for i in range(len(parents_lst)):
            while True:
                pass