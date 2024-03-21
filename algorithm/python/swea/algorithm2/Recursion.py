# def pys(x):
#     if x==6:
#         return
    
#     print(x,end=' ')
#     pys(x+1)
#     print(x,end=' ')

# pys(0)
import sys
sys.setrecursionlimit(10**6)
# path = []
# visited = [0] * 7
# def permutations(x):
#     if x == 3:
#         print(path)
#         return
    
#     for i in range(1,7):
#         if not visited[i] and not path or path and path[-1] < i:
#             visited[i]=1
#             path.append(i)
#             permutations(x+1)
#             path.pop()
#             visited[i]=0

# permutations(0)
path = []
N = 0
def type1(x):
    if x==N:
        print(*path)
        return
    
    for i in range(1,7):
        path.append(i)
        type1(x+1)
        path.pop()

def type2(x):
    if x==N:
        print(*path)
        return
    
    for i in range(1,7):
        if used[i] == True: continue
        used[i] = True
        path.append(i)
        type2(x+1)
        path.pop()
        used[i] = False

used = [False for _ in range(7)]
N,type = map(int,input().split())
if type == 1:
    type1(0)
if type == 2:
    type2(0)