N = int(input())
number = 666
answer = 0

# 정답이 나올 때 까지 돌린다..
while True:
    if '666' in str(number):
        answer += 1

        # 666이 들어간 것이 N번째 나왔을 때 number 이 정답
        if answer == N:
            print(number)
            break
    number += 1