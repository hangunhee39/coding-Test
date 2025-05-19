N, M = map(int, input().split())

s = set()
answer = 0

for _ in range(N):
    s.add(input())
    
for _ in range(M):
    if input() in s :
        answer += 1
        
print(answer)