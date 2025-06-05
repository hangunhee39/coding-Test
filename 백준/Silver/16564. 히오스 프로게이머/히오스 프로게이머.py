N, K = map(int, input().split())
arr = [int(input()) for _ in range(N)]

start = min(arr)
end = start + K

answer = start
while start <= end:
    mid = (start + end) // 2

    current = 0
    for x in arr:
        if x < mid:
            current += (mid - x)

    if current <= K:
        start = mid + 1
        answer = max(answer, mid)
    else :
        end = mid - 1

print(answer)