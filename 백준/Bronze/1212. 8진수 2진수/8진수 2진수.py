from collections import deque

item = [int(i) for i in input()]
answer = []

for i in item :
    q = deque()
    for _ in range(3) :
        q.appendleft(i % 2)
        i = i //2
    answer.append("".join(map(str, q)))

print(int("".join(answer)))

# 파이썬 내장 함수 8 -> 2
# print(bin(int(input(), 8))[2:])