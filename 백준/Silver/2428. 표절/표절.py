# 이분탐색

n = int(input())
arr = sorted(list(map(int, input().split())))

answer = 0
for i in range(n):
    start, end = i, n-1

    while start <= end:
        mid = (start + end) // 2

        if arr[i] < 0.9 * arr[mid] :
            end = mid - 1
        else :
            start = mid + 1

    answer += start -1 - i
print(answer)