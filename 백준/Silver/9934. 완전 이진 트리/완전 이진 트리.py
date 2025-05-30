K = int(input())
arr = list(map(int, input().split()))
tree = [[] for _ in range(K)]

def dfs(start, end, level):
    mid = (start + end) // 2
    tree[level].append(arr[mid])
    
    if start == end:
        return

    dfs(start, mid - 1, level + 1)
    dfs(mid + 1, end, level + 1)

dfs(0, len(arr)-1, 0)

for answer in tree:
    print(*answer)