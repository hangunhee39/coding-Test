#정수론
#1  2   3   4   5   6   7   8   9   10
#o  o   o   o   o   o   o   o   o   0
#   x       x       x       x       x
#       x           0           x   
#           o               o           
#               x                   0
#                   x                   
#                       x               
#                           x           
#                               o   
#                                   x
# => 제곱 수만 o 이다

n = int(input())

answer = int(n**0.5)

print(answer)