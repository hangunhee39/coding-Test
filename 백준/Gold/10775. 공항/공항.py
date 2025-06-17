import sys
input = sys.stdin.readline

G = int(input())
P = int(input())
parent = [i for i in range(G+1)]
answer = 0

# 유니온 파인드 해야 하는 이유: 시간초과, (경로 압축이 유리한 구조)
# 경로가 차면 앞에꺼랑 연결시키면 빠른 시간안에 찾을 수 있음
def _find(a):
    if a == parent[a]:
        return a
    else:
        parent[a] = _find(parent[a])
        return parent[a]

def _union(a, b):
    a = _find(a)
    b = _find(b)
    if a == b:
        return
    parent[a] = b

for _ in range(G):
    g = int(input())
    parent_g = _find(g)

    # 부모가 0이면 이미 게이트가 꽉찬거다
    if parent_g == 0:
        break
        
    # 게이트와 연결하면 부모를 하나 줄인걸 연결한다 (다음 같은거 대비)
    _union(parent_g, parent_g - 1)
    answer += 1
    
print(answer)
    
    