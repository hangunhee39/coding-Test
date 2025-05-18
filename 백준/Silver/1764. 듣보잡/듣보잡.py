N, M = map(int, input().split())
arr1 = set()
arr2 = set()

for i in range(N):
    arr1.add(input())

for i in range(M):
    arr2.add(input())

answer = sorted(arr1 & arr2)

print(len(answer))
print("\n".join(answer))
    
    