N, K = map(int, input().split())

# 등차수열의 합 (공차 1)
AP = K*(K+1)//2

if N < AP:
    print(-1) # 팀 수가 더 커야 담을 수 있음
else :
    # if) N = 11 , AP = 8 , K = 3
    # 2,3,4 -> 2,4,5 - 뒤에를 늘린다 (K로 나눴을 때 나머지 만큼 뒤에서)
    # K로 나눴을 때 나머지가 있으면 + 1
    if (N - AP) % K == 0:
        print(K - 1) 
    else :
        print(K) # 무조건 k 이상 넘을 순 없다 (조건, 최소가 되도록 담음)
