# 트리 
# 1. 모든 노드들은 연결되어 있어야 한다
# 2. 사이클이 발생하면 안된다

# 조상이 정해져 있으면 = 루티드 트리
# 없으면 = 트리 -> 조상을 바꿔가면서 계산해라!

#dfs - preorder(부모 -> 자식, 데이터 전달 가)
#dfs - inorder(완전 이진 트리 아니고 서야 활용 쉽지 않음)
#dfs - postorder(자식 -> 부모, 데이터 전달 가)

#양반향 , 부모가 뭔지 모름
import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**6) 
N = int(input())

graph = [[] for _ in range(N+1)]
parent = [0 for _ in range(N+1)] #부모 정보 저장

#자식 개수 구하기 
child_num = [0 for _ in range(N+1)]

for _ in range(N-1) :
    a, b = map(int, input().split())
    # 어느쪽이 부모인지 모름 -> 
    # (양방향) 두 쪽에 저장, 역주행 방지는 밑에서
    graph[a].append(b)
    graph[b].append(a)

   

# dfs - preorder (부모에서 자식으 정보 넘기기 - 부모 찾기)
def recur(node, prv) :
    parent[node] = prv
    for next in graph[node] :
        # 역주행 방지 , (무한 재귀 방지)
        if next == prv:
            continue
        recur(next, node)
        
    #postorder (자식 수 구하기)
    child_num[prv] += 1
    
    
recur(1,0)

for i in range(2, N+1):
    print(parent[i])
    
#print(child_num)