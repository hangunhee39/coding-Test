N = int(input())
arr = list(map(int, input().split()))

answer = 0
start = 0
end = N-1

while start < end:
    answer = max(answer, (end - start-1)*min(arr[end], arr[start]))

    # 사이 개수는 어쩌피 줄어듬, 그나마 능력치가 높은걸 유지 시켜야함
    if arr[start] < arr[end]:
        start += 1
    else:
        end -= 1
        
print(answer)