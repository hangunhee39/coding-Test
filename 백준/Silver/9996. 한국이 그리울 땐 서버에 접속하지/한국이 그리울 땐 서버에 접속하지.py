N = int(input())
front , back = input().split('*')

for _ in range(N) :
    name = input()
    if name[:len(front)] == front and name[-(len(back)):] == back and len(name) >= len(front) + len(back):
        print("DA")
    else :
        print("NE")