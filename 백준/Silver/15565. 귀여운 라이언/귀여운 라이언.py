# 투 포인터
# 라이언의 위치를 인덱스 리스트로 만들고
#  슬라이싱 윈도를 사용해서 start, end 둘 다 +1

N, K = map(int, input().split())
arr = list(map(int, input().split()))

lion_idx_arr =[]
for idx in range(N) :
    if arr[idx] == 1 :
        lion_idx_arr.append(idx)
        
start = 0
end =  K-1
answer = 1_000_001

if len(lion_idx_arr) < K :
    print(-1)
    exit(0)

for _ in range(len(lion_idx_arr) - K + 1):
    length = lion_idx_arr[end] - lion_idx_arr[start] + 1
    answer = min(answer, length)
    start += 1
    end += 1
    
print(answer)