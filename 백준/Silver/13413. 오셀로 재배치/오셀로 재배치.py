# 그리드 알고리즘
# 만약에 다른 곳에 백 1 흑 1개면 -> 교환(1번)으로 가능
# 따라서 그냥 다른 곳 중에 흑, 백 개수가 큰 것이 답

T = int(input())
for _ in range(T) :
    N = int(input())
    b_count = 0
    w_count = 0
    begin = list(input())
    goal = list(input())

    for i in range(N) :
        if begin[i] != goal[i]:
            if begin[i] == 'W':
                w_count += 1
            else :
                b_count += 1

    print(max(b_count, w_count))
        
        