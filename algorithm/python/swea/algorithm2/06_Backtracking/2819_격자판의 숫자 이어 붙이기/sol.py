import sys
sys.stdin = open('input.txt')

dr = [(1,0),(0,1),(-1,0),(0,-1)]

def dfs(x,y,result):
    global cnt
    if len(result)==7:
        if result not in temp:
            cnt+=1
            temp.add(result)
        return

    for i in range(4):
        nx = x + dr[i][0]
        ny = y + dr[i][1]
        if 0<= nx < 4 and 0<=ny<4 and not visited[nx][ny]:
            dfs(nx,ny,result + arr[nx][ny])

for tc in range(1,int(input())+1):
    temp =set()
    cnt = 0
    visited = [[0] * 4 for _ in range(4)]
    arr = [input().split() for _ in range(4)]
    for i in range(4):
        for j in range(4):
            dfs(i,j,str(arr[i][j]))
    print(f'#{tc} {cnt}')