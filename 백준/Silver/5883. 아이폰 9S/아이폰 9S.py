N = int(input())
arr = [int(input()) for _ in range(N)]
s = set(arr)
answer = 1

for num in s:
    count = 1
    perv = 0
    for current in range(1,N):
        if arr[current] == num:
            continue
        elif arr[current] == arr[perv]:
            count += 1
            answer = max(answer, count)
        else :
            count = 1
            
        perv = current
print(answer)