N = int(input())
arr = input().strip()
dict = {"R": 0, "B": 0}

pre = ''
for color in arr:
    if color != pre:
        dict[color] += 1
    pre = color

answer = min(dict['B'], dict['R'])

print(answer + 1)
        
    
    