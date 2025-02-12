item = list(input().strip())

# 대칭인 지점을 찾는다
# tip - 끝점은 항상 포함해야 한다

for i in range(len(item)):
    # 어쩌피 마지막에는 무조건 걸림(한글자)
    # item[i:][::-1] -> list(reversed(item[i:])) 으로 가능
    if item[i:] == item[i:][::-1]:
        print(len(item) + i) 
        break
        