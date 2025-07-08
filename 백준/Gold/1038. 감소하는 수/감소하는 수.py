from itertools import combinations

N = int(input())
answer = []

# 경우의 수를 구할 때엔 반사적으로 백트래킹, 그리고 itertools 를 떠올리자
for i in range(1, 11):
    # 0 ~ 9 중 i개를 선택해서 만들 수 있는 수열을 거꾸로 정렬 (감소하는 수)
    for comb_arr in combinations(range(0, 10), i):
        tmp = sorted(comb_arr, reverse = True)
        answer.append(int("".join(map(str, tmp))))

answer.sort()
if len(answer) > N:
    print(answer[N])
else :
    print(-1)
    
