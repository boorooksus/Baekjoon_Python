from sys import stdin

#========== 3 =========================================
def palindrome(x):
    #============= 1 ===================================
    x += 1
    #int를 각 자리수 별로 리스트에 저장
    x_list = list(int(i) for i in str(x))
    # l : 리스트의 길이
    l = len(x_list)

    #답이 나올때까지 반복
    while(1):
        #바뀐게 있는지 확인하는 변수(바뀐게 없으면 반복문 빠져나옴)
        isChanged = False
        #이제부터 각 자리수별로 같도록 만들 것인데
        #길이의 반만 확인하면 됨
        for i in range(l // 2):
            fidx = i #리스트 앞쪽 숫자의 인덱스
            bidx = l - i - 1 #리스트 뒤쪽 숫자의 인덱스

            #숫자가 같다면 continue
            if x_list[fidx] == x_list[bidx]:
                continue
            #뒤쪽의 숫자가 앞쪽의 숫자보다 크다면
            #뒤쪽의 숫자를 앞쪽의 숫자로 바꾸고 bidx에 있는 값에 1을 더해줌
            elif x_list[fidx] < x_list[bidx]:
                isChanged = True
                x_list[bidx - 1] += 1
                x_list[bidx] = x_list[fidx]
            #뒤쪽의 숫자가 앞쪽의 숫자보다 작다면 그냥 뒷쪽의 숫자만 바꿔줌
            else:
                isChanged = True
                x_list[bidx] = x_list[fidx]

            #========== 2 ========================================================
            #리스트의 값 중 한자리수가 아닌 값을 찾아서 그 이전 인덱스의 값에 올려줌
            for j in range(l - 1, -1, -1):
                if x_list[j] > 9:
                    x_list[j - 1] += x_list[j] // 10
                    x_list[j] %= 10

        #더이상 바뀐게 없다면 팰런드롬 수 완성
        if isChanged == False:
            #출력
            ans = 0
            for i in range(l):
                ans = ans * 10 + x_list[i]
            print(ans)
            return



n = int(stdin.readline())
palindrome(n)

#문해기 5주차 1번 유형
# 1 : 문제 조건이 x보다 큰 수중에서 팰런드럼 수를 찾는 것이므로 x가 팰런드럼이라도 출력하면 안됨
# 2 : 이전 버전에서는 이 부분을 for문 첫부분에 체크했는데 그러면 조건에 맞는 팰런드럼이 안나올 수 있음
    # + 초기 버전에서 이거 생각 못해서 while 루프 못 빠져나와서 시간초과
# 3 : 1버전에서는 x에 1씩 증가시키면서 팰런드롬 수 인지 체크했는데
    #그러면 시간초과
