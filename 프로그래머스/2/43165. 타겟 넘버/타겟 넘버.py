def solution(numbers, target):
    answer = 0
    bfs = [0]
    
    for i in numbers:
        temp = []
        
        for j in bfs:
            temp.append(j + i)
            temp.append(j - i)
        bfs = temp
    
    for current in bfs :
        if current == target :
            answer += 1
            
    return answer