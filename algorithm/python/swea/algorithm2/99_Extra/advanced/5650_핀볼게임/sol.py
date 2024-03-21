import sys
sys.stdin = open('input.txt')

block = {1:{1:0,2:3},2:{2:1,3:0},3:{0:1,3:2},4:{0:3,1:2},5:{}}
dr = [(0,1),(1,0),(0,-1),(-1,0)]
<<<<<<< HEAD
=======

>>>>>>> refs/remotes/origin/master
def finds_hole(arr):
    for i in range(N):
        for j in range(N):
            idx = arr[i][j]
            if 6 <= idx <= 10:
                worm_hole[idx].add((i,j))

def DFS(x,y,dir):
    cnt = 0
    original_x, original_y = x,y
    while 1:
        nx = x + dr[dir][0]
        ny = y + dr[dir][1]
<<<<<<< HEAD

        if [original_x,original_y] == [x,y] and cnt or arr[nx][ny]==-1:
            return cnt
        if not (0<= nx < N and 0<= ny < N) or arr[nx][ny]==5:
            cnt += 1
            dir = (dir + 2) % 4
            return 2*cnt-1
        else:
            next = arr[nx][ny]
            if next ==0:
                x,y= nx, ny
            elif 1 <=next <= 4:
                dir = block[next].get(dir, (dir + 2) % 4)
                x,y = nx,ny
                cnt += 1
            elif 6 <= next <= 10:
                x,y = list(worm_hole[next]-{(nx,ny)})[0]
=======
        if [original_x,original_y] == [nx,ny]:
            return cnt
        if not (0<= nx < N and 0<= ny < N) or arr[nx][ny]==5:
            cnt += 1
            return 2*cnt-1
        else:
            if arr[nx][ny] == -1:
                return cnt
            elif arr[nx][ny] == 0:
                x, y= nx, ny
            elif 1 <= arr[nx][ny] <= 4:
                dir = block[arr[nx][ny]].get(dir)
                cnt += 1
                if dir == None:
                    return cnt*2-1
                x,y = nx,ny
            elif 6 <= arr[nx][ny] <= 10:
                x,y = list(worm_hole[arr[nx][ny]]-{(nx,ny)})[0]
>>>>>>> refs/remotes/origin/master
    return cnt

for tc in range(1,int(input())+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    worm_hole = {i: set() for i in range(6, 11)}
    finds_hole(arr)
    max_val = 0
    for i in range(N):
        for j in range(N):
<<<<<<< HEAD
            if arr[i][j] == 0:
=======
            if arr[i][j] ==0:
>>>>>>> refs/remotes/origin/master
                for k in range(4):
                    max_val = max(max_val,DFS(i,j,k))
    print(f"#{tc} {max_val}")
