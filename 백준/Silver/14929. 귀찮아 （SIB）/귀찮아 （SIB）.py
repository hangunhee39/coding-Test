# 누적합
# x1y2 + x1y3 + x1y4 ..... xNyN-2 + xNyN
# -> x1(y1 + y2 + ... yN) + x1(y2 + .. yN) + xN-1yN

# 누적합에서 맨 뒤랑 앞 부분 빼면 y2 + y3 +... yN 구해짐

N = int(input())
arr = list(map(int, input().split()))
prefix = [arr[0]]
answer = 0

for i in range(1, N) :
    #누적합 저장
    prefix.append(prefix[i-1] + arr[i])

for i in range(N) :
    # 맨 뒤랑 앞 부분 빼서 나머지 합 구하기
    answer += arr[i] * (prefix[N-1] - prefix[i]) 
    
print(answer)