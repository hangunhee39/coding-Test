# 투 포인터

N, K = map(int, input().split())
arr = list(map(int, input().split()))
cnt = [0]*(max(arr) + 1)

start = 0
end = 0
answer = 0

while end < N:
    if cnt[arr[end]] < K:
        cnt[arr[end]] += 1
        end += 1
    else :
        cnt[arr[start]] -= 1
        start += 1
    
    answer = max(answer, end - start)

print(answer)    