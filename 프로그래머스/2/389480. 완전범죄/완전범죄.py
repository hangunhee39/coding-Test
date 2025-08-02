def solution(info, n, m):
    global answer
    answer = n
    visited = [] # dfs 경로를 다 담는다 kick
    
    def dfs(i, a, b):
        global answer
        visited.append([i,a,b])
        
        # 문제 조건
        if a >= n or b >= m :
            return
        # a가 현재 답보다 커지면 굳이 더 진행 할 필요 없음 (시간 초과)
        if a >= answer:
            return
        
        if i == len(info):
            answer = a
            return
        
        if i < len(info) :
            if [i+1, a+info[i][0] ,b] not in visited :
                dfs(i+1, a+info[i][0], b)
            if [i+1, a, b+info[i][1]] not in visited :
                dfs(i+1, a, b+info[i][1])
    
    dfs(0,0,0)
    if answer == n:
        return -1
    else:
        return  answer