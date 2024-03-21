import sys
sys.stdin = open('input.txt')
from heapq import *
dr = [(0,1),(1,0),(0,-1),(-1,0)]
def dijkstra(x,y):
    heap = []
    dist[x][y] = 0
    heappush(heap,(0,x,y))
    while heap:
        weight, x, y = heappop(heap)
        for dx,dy in dr:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0<=ny<N:
                new_weight = weight + max(0,arr[nx][ny] - arr[x][y]) + 1
                if dist[nx][ny] > new_weight:
                    dist[nx][ny] = new_weight
                    heappush(heap,(new_weight,nx,ny))

for tc in range(1,int(input())+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    dist = [[2001] * N for _ in range(N)]
    dijkstra(0,0)
    print(dist)
    print(f'#{tc} {dist[-1][-1]}')