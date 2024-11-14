n = int(input())

hint = [list(map(int, input().split())) for _ in range(n)]

ans = 0

for a in range(1, 10):
    for b in range(1, 10):
        for c in range(1, 10):

            if a == b or b == c or c == a:
                continue

            count = 0

            for arr in hint:

                ball_count = 0
                strike_count = 0

                number = list(map(int, str(arr[0])))
                target_strike = arr[1]
                target_ball = arr[2]

                # 스트라이크 계산
                if number[0] == a:
                    strike_count += 1
                if number[1] == b:
                    strike_count += 1
                if number[2] == c:
                    strike_count += 1

                # 볼 계산
                if number[0] in [b, c]:
                    ball_count += 1
                if number[1] in [a, c]:
                    ball_count += 1
                if number[2] in [a, b]:
                    ball_count += 1

                if ball_count != target_ball or strike_count != target_strike:
                    break
                count += 1

            if count == n:
                ans += 1

print(ans)
