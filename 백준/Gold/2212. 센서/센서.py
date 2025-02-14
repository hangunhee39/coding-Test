N = int(input())
K = int(input())
cctv = list(map(int, input().split()))
cctv.sort()
between = []
for i in range(1,N):
    between.append(cctv[i]-cctv[i-1])
between.sort()

# K-1 개를 빼야한다 (2집중국이면 젤 긴 cctv 사이 거리만 빼면 된다)
print(sum(i for i in between[0:N-K]))
    