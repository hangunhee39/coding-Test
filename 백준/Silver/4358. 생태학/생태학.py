# 1. Counter 사용하기

from collections import Counter
import sys
input = sys.stdin.readline

arr = []
total = 0

while True :
    tree = input().rstrip()
    if not tree:
        break
    arr.append(tree)
    total += 1

# items를 안하면 키로만 정렬이 됨
# -> key, value 쌍으로 정렬하기 위해 필요 
arr = sorted(Counter(arr).items()) # 결과를 튜플로 된 리스트

for i in range(len(arr)) :
    print("%s %.4f" %(arr[i][0], arr[i][1]/total * 100))
        