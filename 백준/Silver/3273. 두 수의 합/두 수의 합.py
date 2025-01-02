#two pointer : 가능성을 지워주는 것 (가능성 없는 것 삭제)
# 정렬  -> two point

N = int(input())
items = sorted(list(map(int, input().split())))
X = int(input())

start = 0
end = N-1

cnt = 0

#토인터가 만날 때
while start < end :
    #정답 조건
    if items[start] + items[end] == X:
       cnt += 1
    if items[start] + items[end] >= X:
        end -= 1 
    else :
        start += 1

print(cnt)