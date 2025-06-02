# 누적합
import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split())) + [1e9]
Q = int(input())

count_sum = [0]*(N+1)

for i in range(1,N+1):
    if arr[i] < arr[i-1]:
        count_sum[i] = count_sum[i-1] + 1
    else :
        count_sum[i] = count_sum[i-1]

for _ in range(Q):
    x, y = map(int, input().split())    
    print(count_sum[y-1] - count_sum[x-1])
