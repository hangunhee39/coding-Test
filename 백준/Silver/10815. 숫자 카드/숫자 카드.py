# 이분 탐색
# - 수열, 또는 범위, 를 반으로 가르기

N = int(input())
items1 = sorted(list(map(int, input().split())))

M = int(input())
items2 = list(map(int, input().split()))


for number in items2 :
    s = 0
    e = N-1
    flag = False
    #교차되지 않는다면    
    while s <= e: 
        mid = (s+e)//2

        if items1[mid] == number :
            flag = True
            break
        elif items1[mid] > number :
            e = mid - 1
        elif items1[mid] < number :
            s = mid + 1
    if flag :
        print(1, end= " ")
    else :
        print(0, end= " ")

