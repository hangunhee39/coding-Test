from collections import deque

N, K = map(int, input().split())
visited = [0] * 100_001
q = deque()
q.append(N)
answer = 0
answer_count = 0

while q:
    current = q.popleft()
    if current == K:
        answer = visited[current]
        answer_count += 1
        continue

    for i in [current-1, current+1, current*2]:
        
        if 0 <= i <= 100_000:
            # 방문하지 않았거나, 이전 칸에서 온 것만 방문 (큐에 삽입)
            if visited[i] == 0 or visited[i] == visited[current] + 1:
                visited[i] = visited[current] + 1
                q.append(i)

print(answer)
print(answer_count)