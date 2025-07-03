N, M = map(int, input().split())
arr = list(map(int, input().split()))

for _ in range(M):
    cmd, a, b = map(int, input().split())
    if cmd == 1:
        arr[a-1] = b
    elif cmd == 2:
        for i in range(a-1, b):
            if arr[i] == 1:
                arr[i] = 0
            else:
                arr[i] = 1
    elif cmd == 3:
        for i in range(a-1, b):
            arr[i] = 0
    elif cmd == 4:
        for i in range(a-1, b):
            arr[i] = 1            
            
print(*arr)