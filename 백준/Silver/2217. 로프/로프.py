N = int(input())
arr = []
for _ in range(N):
    arr.append(int(input()))

arr.sort(reverse = True)
answer = 0

for i in range(N):
    answer = max(answer, arr[i]*(i+1))

print(answer)