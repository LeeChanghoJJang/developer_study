import sys
sys.stdin = open('input.txt')
from collections import deque
# 주어진 x,y 위치의 터널 모양에 따라 그 다음으로 이동할 수 있는 dx,dy의 인덱스(방향)을 반환하는 함수
movement = {0:[],1:[0,1,2,3],2:[1,3],3:[0,2],4:[0,3],5:[0,1],6:[1,2],7:[2,3]}
# 이전 방향에 따라 받을 수 있는 터널 모양
fits = {0:[1,3,6,7],1:[1,2,4,7],2:[1,3,4,5],3:[1,2,5,6]}
# 델타 설정
dx = [0,1,0,-1]
dy = [1,0,-1,0]

def BFS(R,C,L):
    # 처음 있는 곳도 카운팅해야 함
    cnt = 1
    queue = deque([[R,C]])
    # 처음 있는 곳도 방문 처리해야함
    visited[R][C] = 1
    if L>1:
        while queue:
            x,y = queue.popleft()
            for i in movement[jiha[x][y]]:
                nx = x + dx[i]
                ny = y + dy[i]
                # 조건1 : 지하터널의 범위 내에 들어오는가
                # 조건2 : 방문한적이 없는가
                # 조건3 : 현재 위치의 터널 모양과 다음으로 이동하는 터널의 모양이랑 이어지는가
                if 0<=nx<N and 0<=ny<M and not visited[nx][ny] and jiha[nx][ny] in fits[i]:
                    cnt +=1
                    visited[nx][ny]= visited[x][y] + 1
                    if visited[nx][ny] == L:
                        continue
                    queue.append([nx,ny])
    return cnt

for tc in range(1,int(input())+1):
    N,M,R,C,L = map(int,input().split())
    jiha = [list(map(int,input().split())) for _ in range(N)]
    visited = [[0] * M for _ in range(N)]
    print(f'#{tc} {BFS(R,C,L)}')
