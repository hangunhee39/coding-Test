N = int(input())
arr = list(map(int, input().split()))
arr_sum = [0] * (N+1)
answer = 0

for i in range(N):
    arr_sum[i+1] = arr_sum[i] + arr[i]

#벌이나 꿀통은 무조건 양끝에 있어야함
# arr(i) == arr_sum(i+1) , 위치 상

for i in range(1, N-1):
    # 1. 꿀통 arr - index 0
    answer = max(answer, arr_sum[i+1] + arr_sum[N] - arr[i]*2 - arr[N-1])
    
    # 2. 꿀통 arr - index i
    answer = max(answer, arr_sum[i+1] + arr_sum[N] - arr_sum[i] - arr[N-1] - arr[0])
    
    # 3. 꿀통 arr - index N
    answer = max(answer, arr_sum[N]*2 - arr_sum[i] - arr[0] - arr[i]*2)

print(answer)