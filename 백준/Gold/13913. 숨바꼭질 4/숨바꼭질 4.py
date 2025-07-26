from collections import deque

N, K = map(int, input().split())
q = deque()
counts = [0] * 100_001
prevs = [0] * 100_001
answer = []
counts[N] = 1
q.append([N,1])

while q:
    cur, c_count = q.popleft()
    if cur == K:
        prev = cur
        print(counts[K]-1)
        while prev != N:
            answer.append(prev)
            prev = prevs[prev]
        answer.append(N)
        print(*answer[::-1])
        break
        
    for next in [cur+1, cur-1, cur*2]:
        if 0 <= next <= 100_000 and counts[next] == 0:
            q.append([next, c_count+1])
            counts[next] = c_count+1
            prevs[next] = cur
        
    