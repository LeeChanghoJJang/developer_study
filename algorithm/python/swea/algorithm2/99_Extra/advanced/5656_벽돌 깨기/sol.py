import sys
sys.stdin = open('input.txt')
from collections import deque
dr = [(0,1),(1,0),(-1,0),(0,-1)]

def downs():
    pass

def distroy(x,y):
    queue = deque([[x,y]])
    while queue:
        x,y = queue.popleft()
        for product in range(1,rocks[x][y]):
            for i in range(4):
                nx = x+dr[i][0] * product
                ny = y+dr[i][1] * product
                if 0<=nx<H and 0<=ny<W:
                    rocks[nx][ny]=0
                    if rocks[nx][ny]>1:
                        queue.append(rocks[nx][ny])
        if





for tc in range(1,int(input())+1):
    N, W, H = map(int,input().split())
    rocks = [list(map(int,input.split())) for _ in range(N)]
