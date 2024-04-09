from collections import deque

###################### 채점기 준비 ######################
Q = int(input()) # number of commands
_, number_judger, domain = input().split() # 100, 3, codetree.ai/16
number_judger = int(number_judger) # number of judgers

# make waiting_judger queue
waiting_judger = deque()
for i in range(number_judger):
    waiting_judger.append(i + 1)

# make queues we need
waiting_queue = deque() # 채점 대기 큐
judging_queue = deque() # 채점 진행 큐
history_queue = deque() # 채점 완료 큐

waiting_queue.append((0, 1, domain))
###################### 채점기 준비 ######################

###################### NEXT ######################
for _ in range(Q - 1):
    ### input ###
    lst = input().split()
    lst[0] = int(lst[0])

    # print(f'lst: {lst}')

    ### 채점 요청 ###
    if lst[0] == 200: # lst : 200, t, p, u : 200, 5, 1, codetree.ai/17
        (t, p, u) = (int(lst[1]), int(lst[2]), lst[3])
        
        # if (t, p, u) not in waiting_queue:
        #     waiting_queue.append((t, p, u))
        
        # 채점 대기 큐에 있는 task 중 u와 일치하는 url이 하나라도 있으면 넘어감
        cnt = 0
        for task in waiting_queue:
            if u == task[-1]:
                break
            else:
                cnt += 1
        
        if cnt != len(waiting_queue):
            # print(f'waiting_queue: {waiting_queue}')
            continue
        else:
            waiting_queue.append((t, p, u))

        # print(f'waiting_queue: {waiting_queue}')
    
    ### 채점 시도 ###
    elif lst[0] == 300: # lst : 300, t : 300, 1
        t = int(lst[1])
        # 우선, 채점 가능한 채점기가 없다면 요청 무시하고 넘어감.
        if not waiting_judger:
            continue

        # t초에 채점 대기 큐에서 즉시 채점이 불가능한 경우를 제외하고 남은 task 중 우선순위가 가장 높은 채점 task를 골라 채점 진행.
        # 방법 1: 채점 불가능한 경우 먼저 제외하고 우선순위와 시간을 기준으로 정렬한 뒤 가장 우선인 task 선택.
        # 방법 2: 우선순위와 시간을 기준으로 먼저 정렬하고 차례차례 채점 가능/불가능 여부 판별하고 채점 가능한 task 선택.

        # 방법 2가 좀 더 좋아보인다.

        # 먼저 정렬
        waiting_queue = sorted(waiting_queue, key=lambda x: (x[1], x[0]))
        # print(f'waiting_queue: {waiting_queue}')

        # 이제 차례차례 채점 가능/불가능 여부 확인하고 가능한 task 나오자마자 선택하면 됨.
        for task in waiting_queue:
            check = True
            # 불가능 경우 1
            dom = task[2].split('/')[0]
            for judging_task in judging_queue:
                if dom == judging_task[1].split('/')[0]:
                    check = False
                    break
            if check == False:
                continue       
            
            # 불가능 경우 2
            for history_task in history_queue:
                if dom == history_task[2].split('/')[0]:
                    start = int(history_task[0])
                    end = int(history_task[1])
                    gap = end - start
                    if t < (start + 3 * gap):
                        check = False
                        break
            if check == False:
                continue
            
            if check == True:
                J_id = waiting_judger.popleft()
                data = waiting_queue.pop(0)
                judging_queue.append((t, data[-1], J_id))
                # print(judging_queue)
                break

    ### 채점 종료 ### (O)
    elif lst[0] == 400: # lst : 400, t, J_id : 400, 4, 1
        # 채점 진행 큐에서 채점 완료 큐로 데이터 이동
        (start, u, J_id) = judging_queue.popleft()
        history_queue.append((start, int(lst[1]), u, J_id))
        # print(f'history_queue: {history_queue}')

        # 채점기 해제
        waiting_judger.insert(J_id-1, J_id)

    ### 채점 대기 큐 조회 ### (O)
    elif lst[0] == 500: # lst : 500, t : 500, 7
        print(len(waiting_queue))
###################### NEXT ######################