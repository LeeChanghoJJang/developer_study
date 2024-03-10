import sys
sys.stdin = open('input.txt')
N,M = map(int,input().split())
temp =[]
def backtrack(temp):
    if len(temp)==M:
        print(*temp)
        return

    for i in range(1,N+1):
        temp.append(i)
        backtrack(temp)
        temp.pop()

backtrack(temp)