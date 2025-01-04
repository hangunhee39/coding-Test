# 이분 탐색
# - 수열, 또는 범위, 를 반으로 가르기

N, M = map(int, input().split())
items = sorted(list(map(int, input().split())))

s= 0
e = max(items)

while s <= e:
    mid = (s+e)//2
    
    # 나무 채취 카운트
    x = 0
    for tree in items:
        if tree >= mid :
            x += tree - mid
        
    # 업, 다운 체크
    if x >= M : #같아도 넘으면 처음 조건문에 걸림
        s = mid + 1
    else :
        e = mid - 1

print(e)