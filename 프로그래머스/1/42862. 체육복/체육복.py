def solution(n, lost, reserve):
    visited = [1] * (n+1)
    reserve.sort()

    for i in lost:
        if i in reserve:
            reserve.remove(i)
        else:
            visited[i] = 0
        
    for i in reserve:
        if visited[i] == 0:
            visited[i] = 1
            continue
        if visited[i-1] == 0:
            visited[i-1] = 1
        elif i+1 <= n and visited[i+1] == 0:
            visited[i+1] = 1
    
    visited[0] = 0
    return sum(visited)