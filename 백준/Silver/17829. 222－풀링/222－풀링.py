N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]

def divdeAndConquer(size, y, x):
    if size == 2:
        tmp = [graph[y][x], graph[y+1][x], graph[y][x+1], graph[y+1][x+1]]
        tmp.sort()
        return tmp[2]

    size //= 2

    leftTop = divdeAndConquer(size, y, x)
    rightTop = divdeAndConquer(size, y, x+size)
    leftBottom = divdeAndConquer(size, y+size, x)
    rightBottom = divdeAndConquer(size, y+size, x+size)

    answer = [leftTop, rightTop, leftBottom, rightBottom]
    answer.sort()
    return answer[2]

print(divdeAndConquer(N, 0, 0))    