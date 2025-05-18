import re

N = int(input())
patten = re.compile('^[A-F]?A+F+C+[A-F]?$')

for _ in range(N):
    s = input()
    if patten.match(s) is None :
        print("Good")
    else :
        print("Infected!")
    
    