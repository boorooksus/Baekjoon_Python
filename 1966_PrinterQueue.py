from sys import stdin
from _collections import deque

t = int(stdin.readline())
for i in range(t):
    ans = 0
    #n : number of jobs in queue
    #m : position of my job
    n, m = map(int, stdin.readline().split())
    #dq : 각 job의 우선순위들 저장
    dq = deque(map(int, stdin.readline().split()))
    #cnt_dict : 각 우선 순위가 dq에 몇 번씩 있는지 저장
    cnt_dict = {}
    for j in dq:
        if j in cnt_dict:
            cnt_dict[j] += 1
        else:
            cnt_dict[j] = 1

    #prt : priority of my job
    prt = dq[m]
    #my job의 priority보다 큰 업무들 수행
    for j in range(9, prt, -1):
        if j not in cnt_dict:
            continue
        while cnt_dict[j] != 0:
            x = dq.popleft()
            if x == j:
                ans += 1
                m -= 1
                # === 1 ===============
                cnt_dict[j] -= 1
            elif m == 0:
                dq.append(x)
                m = len(dq) - 1
            else:
                dq.append(x)
                m -= 1
    #my job과 priority가 같으면서 my job보다 앞에 있는 job 수행
    # === =================
    for j in range(m + 1):
        if dq[j] == prt:
            ans += 1
    print(ans)


#문해기 3주차 유형
# 1 : 카운트 값 안빼주면 무한 루프
# 2 : 이거 안하면 우선순위 낮아도 my job보다 앞에있으면 프린트함함