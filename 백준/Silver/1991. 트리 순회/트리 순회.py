# 트리 
# 1. 모든 노드들은 연결되어 있어야 한다
# 2. 사이클이 발생하면 안된다

# 조상이 정해져 있으면 = 루티드 트리
# 없으면 = 트리 -> 조상을 바꿔가면서 계산해라!

N = int(input())

#아스키 코드 수
graph = [[] for _ in range(130)]

for _ in range(N) :
    a, b, c = map(str, input().split())
    #아스키 코드
    a = ord(a)
    b = ord(b)
    c = ord(c)

    graph[a].append(b)
    graph[a].append(c)

#dfs - preorder(부모 -> 자식, 데이터 전달 가)
def preorder(node) :
    if node == 46: # . == 46
        return
    print(chr(node), end="")
    preorder(graph[node][0])
    preorder(graph[node][1])
    
#dfs - inorder(완전 이진 트리 아니고 서야 활용 쉽지 않음)
def inorder(node) :
    if node == 46: # . == 46
        return
    inorder(graph[node][0])
    print(chr(node), end="")
    inorder(graph[node][1])

#dfs - postorder(자식 -> 부모, 데이터 전달 가)
def postorder(node) :
    if node == 46: # . == 46
        return
    postorder(graph[node][0])
    postorder(graph[node][1])
    print(chr(node), end="")

preorder(65)
print()
inorder(65)
print()
postorder(65)