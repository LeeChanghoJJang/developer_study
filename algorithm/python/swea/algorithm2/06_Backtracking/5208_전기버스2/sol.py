import sys
sys.stdin = open('input.txt')
sys.setrecursionlimit(100000)
def dfs(start,cnt):
    global min_val
    if start + stations[start] >= N-1:
        if min_val > cnt:
            min_val = cnt
        return
    if cnt > min_val:
        return

    for i in range(1,stations[start]+1):
        dfs(start+i,cnt+1)

for tc in range(1,int(input())+1):
    N, *stations = map(int,input().split())
    min_val = int(1e9)
    dfs(0,0)
    print(f'#{tc} {min_val}')