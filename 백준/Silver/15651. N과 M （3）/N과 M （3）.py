# 재귀함수 , 완전탐색 , 백트래킹
# 재귀함수가 for 반복문 보다 자유도가 높다

#number 는 반복 할 횟수 m 까지, output은 출력할 데이터 점점 쌓임 n 까지
def recur(number,output):
    if number == m:
        print(output)
        return
    
    for i in range(1, n+1):
        recur(number+1,output+str(i)+" ") 
        #1 1,2,3,4
        #2 1,2,3,4
        # ....
        


n ,m = map(int,input().split())

recur(0,"")

# m 만큼 반목문을 만들어야함.... 
#for i in range(1,n+1):
#    for i in range(1,n+1):
#        for i in range(1,n+1):