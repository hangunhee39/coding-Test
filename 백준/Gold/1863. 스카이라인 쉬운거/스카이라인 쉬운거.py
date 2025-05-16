n = int(input())
stack = []
answer = 0

for i in range(n):
    w, h = map(int, input().split())

    # 높이가 낮아지면 카운트 + 1
    while stack and stack[-1] > h:
        stack.pop()
        answer += 1

    # 높이가 같은거 무시
    if stack and stack[-1] == h:
        continue
    stack.append(h)

# 높 -> 높 -> 낮 인 경우 카운트 1만 되고 처음 높인 경우를 카운트 하기 위해서
while stack:
    if stack[-1] > 0:
        answer += 1
    stack.pop()
        
print(answer)