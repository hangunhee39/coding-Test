N = int(input())
arr = list(map(int, input().split()))
target = int(input())

start = 0
end = max(arr)
answer = 0

while start <= end:
    mid = (start + end) //2

    tmp = 0
    for item in arr:
        if mid < item:
            tmp += mid
        else :
            tmp += item

    if tmp <= target:
        answer = mid
        start = mid + 1
    else :
        end = mid - 1
        
print(answer)