N, C, W = map(int, input().split())
arr = [int(input()) for _ in range(N)]
answer = 0

for length in range(1, max(arr) + 1):
    cost_tmp = 0

    for tree in arr:
        tree_count =  tree // length
        if tree % length == 0:
            cut_count = tree_count - 1
        else :
            cut_count = tree_count

        cost = (length * tree_count * W) - (cut_count * C)
        if cost > 0:
            cost_tmp += cost
        
    answer = max(answer, cost_tmp)
    
print(answer)