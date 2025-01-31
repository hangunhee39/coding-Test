# 스택
# (K번 만) 앞에서 앞뒤로 비교한다, 어짜피 앞이 중요하기 때문에
# 만약, N-K 길이보다 크면 뒤에서만 빼준다

N, K = map(int, input().split())
number = [ int(i) for i in input().strip()]
stack = [number[0]]

for i in range(1,N):
    # 앞뒤 비교 (K)
    # stack -> 스택이 비어있으면 False
    while K > 0 and stack and stack[-1] < number[i]:
        stack.pop()
        K -= 1
    stack.append(number[i])

# 길이 맞추기
while K > 0:
    stack.pop()
    K -= 1

print(''.join(map(str, stack)))