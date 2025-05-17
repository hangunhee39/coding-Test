n, L = map(int, input().split())
arr = list(map(int, input().split()))

sum = 0

# 위에서 부터 해야함
for i in range(n-1, 0, -1):

    # 무게가 쌓일 수록 중심이 바뀜
    sum += arr[i]
    center = sum / (n-i)

    if center > arr[i-1]-L and center < arr[i-1]+L :
        continue
    else :
        print('unstable')
        exit()
        
print('stable')