# 재귀함수 , 완전탐색 , 백트래킹
# 재귀함수가 for 반복문 보다 자유도가 높다

#number 는 반복 할 횟수 m 까지, output은 출력할 데이터 점점 쌓임 n 까지
def recur(number):
    if number == m:
        print(*arr)
        return
    
    for i in range(1, n+1):
        if i in arr: #중복인거 제외하기
            continue
        arr.append(i)
        recur(number+1) 
        arr.pop()
        
        #1 2,3,4
        #2 1,3,4
        # ....
        


n ,m = map(int,input().split())
arr = []

recur(0)

# m 만큼 반목문을 만들어야함.... 
#for i in range(1,n+1):
#    for i in range(1,n+1):
#        for i in range(1,n+1):
            