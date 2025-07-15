from itertools import permutations

def solution(numbers):
    tmp = []
    
    for i in range(1, len(numbers) + 1):
        tmp += list(permutations(numbers, i))
    
    nums = set([int(''.join(p)) for p in tmp ])
    

    prime = [True] * 10_000_000
    for i in range(2, 10_000_000):
        if prime[i] :
            for j in range(i*2, 10_000_000, i):
                prime[j] = False
    prime[1] = False
    prime[0] = False
    
    answer = 0
    
    for num in nums:
        if prime[num]:
            answer += 1

    return answer