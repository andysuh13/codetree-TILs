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
    t = int(lst[1])
    ### 채점 요청 ###
    if lst[0] == 200: # lst : 200, t, p, u : 200, 5, 1, codetree.ai/17
        (p, u) = (int(lst[2]), lst[3])
    
        # 채점 대기 큐에 있는 task 중 u와 일치하는 url을 갖는 task가 있는지 확인
        cnt = 0
        for task in waiting_queue:
            # 같은 task가 발견되면 break
            if u == task[-1]:
                break
            # 같은 task가 아니면 cnt += 1, 즉, cnt는 u와 다른 url을 갖는 task의 갯수를 의미.
            else:
                cnt += 1
        
        # 만약, cnt가 채점 대기 큐의 길이랑 다르다면, 이는 같은 task가 있다는 얘기가 되므로 요청 무시하고 넘어감.
        if cnt != len(waiting_queue):
            continue
        # cnt가 채점 대기 큐의 길이와 같다면, 이는 같은 task가 없다는 얘기이므로 채점 대기 큐에 추가한다.
        else:
            waiting_queue.append((t, p, u))
            continue
    
    ### 채점 시도 ###
    elif lst[0] == 300: # lst : 300, t : 300, 1

        # 우선, 채점 가능한 채점기가 없다면 요청 무시하고 넘어감.
        if not waiting_judger:
            continue

        # t초에 채점 대기 큐에서 즉시 채점이 불가능한 경우를 제외하고 남은 task 중 우선순위가 가장 높은 채점 task를 골라 채점 진행.
        # 방법 1: 채점 불가능한 경우 먼저 제외하고 우선순위와 시간을 기준으로 정렬한 뒤 가장 우선인 task 선택.
        # 방법 2: 우선순위와 시간을 기준으로 먼저 정렬하고 차례차례 채점 가능/불가능 여부 판별하고 채점 가능한 task 선택.

        # 방법 2가 좀 더 좋아보인다.

        # 먼저 정렬
        waiting_queue = sorted(waiting_queue, key=lambda x: (x[1], x[0]))

        # 이제 차례차례 채점 가능/불가능 여부 확인하고 가능한 task 나오자마자 선택하면 됨.
        for task in waiting_queue:
            check = True
            # 불가능 경우 1 : 현재 채점하려는 task의 도메인이 채점 중인 task들의 도메인 중 하나일 경우
            dom = task[2].split('/')[0] # codetree.ai
            for judging_task in judging_queue:
                if dom == judging_task[1].split('/')[0]:
                    check = False
                    break
            if check == False:
                continue       
            
            # 불가능 경우 2: 현재 채점하려는 task의 도메인과 같은 도메인에 대해 가장 최근에 진행된 채점 시간을 start, 종료 시간을 start + gap이라 할 때, t < start + 3 x gap인 경우
            for history_task in history_queue:
                if dom == history_task[2].split('/')[0]:
                    start = int(history_task[0])
                    end = int(history_task[1])
                    gap = end - start
                    if t < (start + (3 * gap)):
                        check = False
                        break
            if check == False:
                continue
            
            if check == True:
                J_id = waiting_judger[0]
                waiting_judger.remove(J_id)
                data = waiting_queue.pop(0)
                judging_queue.append((t, data[-1], J_id))
                # print(judging_queue)
                break

    ### 채점 종료 ### (O)
    elif lst[0] == 400: # lst : 400, t, J_id : 400, 4, 1
        J_id = int(lst[2])

        # 채점 중인 task가 없다면, 요청 무시하고 넘어감.
        if not judging_queue:
            continue

        # J_id번 채점기가 진행하고 있는 채점이 없다면 요청 무시하고 넘어가고, 있다면 채점 완료 처리.
        # 
        for judging_task in judging_queue:
            # J_id번 채점기가 진행하고 있는 채점이 있는지 확인
            # J_id번 채점기가 진행하고 있는 채점이 아니라면, pass
            if J_id != judging_task[2]:
                continue
            # J_id번 채점기가 진행하고 있는 채점이 있다면, 채점 종료 시켜야 함.
            else:
                (start, u, J) = judging_task
                # 채점 완료 기록 큐에 추가
                history_queue.append((start, t, u, J))
                break
        # 채점 진행 큐에서 삭제
        judging_queue.remove(judging_task)
        

        # 채점기는 다시 쉬는 상태로 반환하고 끝.
        waiting_judger.append(J_id)
        waiting_judger = sorted(waiting_judger)
        continue

    ### 채점 대기 큐 조회 ### (O)
    elif lst[0] == 500: # lst : 500, t : 500, 7
        print(len(waiting_queue))
        continue
###################### NEXT ######################