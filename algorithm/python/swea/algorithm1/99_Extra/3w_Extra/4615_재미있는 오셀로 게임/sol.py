import sys
sys.stdin = open('input.txt')
T = int(input())

dx = [0,1,0,-1,1,1,-1,-1]
dy = [1,0,-1,0,1,-1,-1,1]
# color가 근처에 있는지, 방향을 확인하는 함수
def nearby_color(coord,color):
    x,y = coord
    temp =[]
    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < N and board[nx][ny] not in [color, 0]:
            temp.append(i)
    return temp

def go_color(temp,coord,color):
    x,y = coord
    board[x][y]=color
    x1,y1=x,y
    for i in temp:
        check = True
        result = []
        x,y=x1,y1
        while 1:
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<N and 0<=ny<N:
                if board[nx][ny] ==0:
                    check = False
                    break
                elif board[nx][ny] == color:
                    break
                else:
                    result.append([nx, ny])
                    x, y = nx, ny
            else:
                check=False
                break
        if check:
            for row,col in result:
                board[row][col] = color
def cnt_color(boards):
    cnt_1 = cnt_2 = 0
    for i in range(N):
        for j in range(N):
            if boards[i][j]==1:
                cnt_1+=1
            elif boards[i][j]==2:
                cnt_2+=1
    return [cnt_1,cnt_2]

for tc in range(1,T+1):
    N,M = map(int,input().split())
    board = [[0] * N for _ in range(N)]
    board[N // 2][N // 2] = 2
    board[N // 2 - 1][N // 2] = 1
    board[N // 2][N // 2 - 1] = 1
    board[N // 2 - 1][N // 2 - 1] = 2
    for _ in range(M):
        y, x, color = map(int,input().split())
        x-=1
        y-=1
        coord = [x,y]
        temp = nearby_color(coord,color)
        go_color(temp,coord,color)
    print(f'#{tc}',end=' ')
    arbitary= cnt_color(board)
    print(*arbitary)





