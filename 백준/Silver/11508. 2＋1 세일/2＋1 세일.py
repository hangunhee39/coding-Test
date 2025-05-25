N = int(input())

arr = [ int(input()) for _ in range(N)]
arr.sort(reverse = True)

answer = sum(arr)

for i in range(N):
    if (i+1)%3 == 0 :
        answer -= arr[i]
        
print(answer)