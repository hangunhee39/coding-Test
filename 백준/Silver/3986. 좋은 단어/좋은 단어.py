N = int(input())
answer = 0

for i in range(N):
    arr = list(input())
    stack = []

    for c in arr:
        if stack and stack[-1] == c:
            stack.pop()
            continue
        stack.append(c)

    if not stack:
        answer += 1

print(answer)