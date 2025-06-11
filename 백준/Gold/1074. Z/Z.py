N, r, c = map(int, input().split())

# size는 전체 모든 수 , val은 4묶음 중 첫번째 값 (4사분면)
def divid(y, x, size, val):
    size //= 2

    # 마지막 빼곤 전부 첫번째에 걸린다
    if y < size and x < size:
        if size == 1:
            print(val)
            exit()
        divid(y, x, size, val)

    elif y < size and x >= size:
        if size == 1:
            print(val + 1)
            exit()
        divid(y, x-size, size, val + size**2 * 1)

    elif y >= size and x < size:
        if size == 1:
            print(val + 2)
            exit()
        divid(y-size, x, size, val + size**2 * 2)

    elif y >=size and x >= size:
        if size == 1:
            print(val + 3)
            exit()
        divid(y-size, x-size, size, val + size**2 * 3)

divid(r, c, 2**N, 0)