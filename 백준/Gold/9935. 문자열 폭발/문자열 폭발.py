#Stack 스택 문제
# 폭탄이 터지면 다음거 비교할려면 남은 스택을 사용해야 함!

S = input().rstrip()
bomb = input().rstrip()

bomb_size = len(bomb)
stack = []

for s in S :
    stack.append(s)
    # 문자열과 문자열 비교해야 함 ("".join 안하면 항상 false)
    if "".join(stack[len(stack) - bomb_size :len(stack)]) == bomb :
        # 폭탄 길이 만큼 pop
        for _ in range(bomb_size) :
            stack.pop()

if len(stack) == 0 :
    print("FRULA")
else :
    print("".join(stack))