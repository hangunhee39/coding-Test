def solution(answers):
    one = [1,2,3,4,5] 
    two = [2,1,2,3,2,4,2,5] 
    three = [3,3,1,1,2,2,4,4,5,5] 
    
    tmp = [0, 0, 0]
    answer = []
    
    for i in range(len(answers)):
        if answers[i] == one[i % len(one)]: 
            tmp[0] += 1
        if answers[i] == two[i % len(two)]:
            tmp[1] += 1
        if answers[i] == three[i % len(three)]:
            tmp[2] += 1
            
    for i in range(3):
        if tmp[i] == max(tmp):
            answer.append(i+1)
    
    return answer