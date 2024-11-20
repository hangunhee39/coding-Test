# 누적함
# 다이나믹 프로그래밍 (메모이제시연)

n = int(input())
arr = list(map(int, input().split()))

prefix = [0 for _ in range(n+1)]

for i in range(n) :
    #누적 합된게 다음 수보다 작으면 굳이 누적합을 이어 나갈 필요 x (연속된 수일때만 가능한 듯)
    prefix[i+1] = max(prefix[i] + arr[i], arr[i]) 

print(max(prefix[1:])) #음수일경우 0이 제일 클수 있음 그래서 인덱스 0 방지