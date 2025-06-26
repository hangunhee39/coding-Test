n = int(input())
arr = [int(input()) for _ in range(n)]
MAX = max(arr)
stack = []
answer = 0

for item in arr:
    # 스택을 통해 중복을 처리
    if stack:
        if stack[-1] < item:
            answer += item - stack.pop()
        else:
            # 스택에 있는 것보다 더 작거나 같은 걸 무시하는 이유
            # 같은거 -> 문제에서 무시
            # 작은거 -> 더 작은게 큰거 만났을 때 다음에 어쩌피 커짐
            stack.pop()
        stack.append(item)
    else:
        stack.append(item)

# 마지막에 작은게 남아있으면 최대에서 뺀 만큼 더함
if stack:
    answer += MAX - stack[-1]

print(answer)
    
    