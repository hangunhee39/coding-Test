N = int(input())
M = int(input())
arr = sorted(list(map(int, input().split())))

start = 0
end = N-1
answer = 0

while start < end:
    if arr[start] + arr[end] == M:
        answer += 1
        end -= 1
    elif arr[start] + arr[end] > M :
        end -= 1
    else :
        start += 1

print(answer)    
    