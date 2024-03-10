# 백준 1022번 소용돌이 예쁘게 출력하기
import sys
from pprint import pprint
sys.stdin = open('input.txt')
# 메모리 초과
x1, y1, x2, y2 = map(int, input().split())
max_num =max(abs(x1),abs(y1),abs(x2),abs(y2))
n= 2*max_num +1
# n=7
def tonado(n):
    dir =0
    dx = [0,-1,0,1] # 왼 위 오 밑
    dy = [-1,0,1,0]
    graph = [[0] * n for _ in range(n)]
    x,y=[n-1,n-1]
    num_count = n**2
    graph[n-1][n-1] = num_count
    while num_count>1:
        nx = x + dx[dir%4]
        ny = y + dy[dir%4]
        if 0<=nx<n and 0<=ny<n and graph[nx][ny]==0:
            num_count-=1
            graph[nx][ny]=num_count
            x,y =nx,ny
        else:
            dir+=1

    return graph
pprint(tonado(n))

for row in range(x1+max_num, x2+max_num+1):
    for col in range(y1+max_num,y2+max_num+1):
        print(f'{tonado(n)[row][col]:2d}',end=' ')
    print()

# 두번째 방법 : 부분배열만 생성하기
r1,c1,r2,c2 = map(int, input().split())
board = [[0]*(c2-c1+1) for _ in range(r2-r1+1)]
board_max = (r2-r1+1) * (c2-c1+1)
x=y=0
num=1
cnt=0
dcnt=1
d=0
dx = [0,-1,0,1] # 왼 위 오 밑
dy = [-1,0,1,0]

while board_max>0:
    if r1 <= y <= r2 and c1 <= x <= c2:
        board_max -= 1
        board[y - r1][x - c1] = num
        max_num = num
    num+=1
    cnt+=1
    x = x + dx[d]
    y = y + dy[d]
    if cnt == dcnt:
        cnt = 0
        d = (d+3)%4
        if d==0 or d==2:
            dcnt+=1

max_num_len = len(str(max_num-1))

for row in range(r2-r1+1):
    for col in range(c2-c1+1):
        print(str(board[row][col]).rjust(max_num_len),end=' ')
    print()