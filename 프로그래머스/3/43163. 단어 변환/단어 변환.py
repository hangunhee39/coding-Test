from collections import deque

def solution(begin, target, words):
    answer = 0
    
    if target not in words:
        return 0
    
    q = deque()
    q.append([begin, 0])
    
    while q:
        tmp, count = q.popleft()
        if tmp == target:
            return count
        
        for word in words:
            count_tmp = 0
            for i in range(len(word)):
                if tmp[i] != word[i]:
                    count_tmp += 1
            # 전에 값이랑 1군데만 다르면 넣는다
            if count_tmp == 1:
                q.append([word, count + 1])




