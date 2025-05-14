# 이진탐색

N = int(input())
M = int(input())
X = list(map(int, input().split()))

# 가로등의 높이
start = 0
end = N
answer = N

def check(cur) :
    if cur - X[0] < 0:
        return False

    if N - X[M-1] > cur:
        return False

    for i in range(1,M):
        if X[i] - X[i-1] > 2*cur:
            return False
            
    return True
        
while start <= end:
    mid = (start + end)//2

    if check(mid) :
        end = mid - 1
        answer = mid
    else :
        start = mid + 1

print(answer)