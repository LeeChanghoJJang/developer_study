import sys
sys.stdin = open('input.txt')
from collections import deque
ways = {1:(-1,0),2:(1,0),3:(0,-1),4:(0,1)}

for tc in range(1,int(input())+1):
    N,M,K = map(int,input().split())
    arr = [[0]*N for _ in range(N)]
    temp = deque([])
<<<<<<< HEAD
    for _ in range(K):
        x, y, cnt, way = map(int, input().split())
        temp.append([x,y,cnt,way])
    for _ in range(M):
        info = {}
        for i in range(K):
            x, y, cnt, way = temp[i]
            nx = x + ways[way][0]
            ny = y + ways[way][1]
            temp[i][0], temp[i][1] = nx,ny
            if nx in [0,N-1] or ny in [0,N-1]:
                if way <=2:
                    way = 3-way
                elif way <=4:
                    way = 7-way
                cnt //=2
                temp[i][2] = cnt
                temp[i][3] = way
            if (nx,ny) not in info.keys():
                info[(nx,ny)] = [i,cnt]
            else:
                num, max_cnt = info[(nx,ny)]
                if temp[i][2] > max_cnt:
                    info[(nx,ny)] = [i,cnt]
                    temp[i][2]+= temp[num][2]
                    temp[num][2] = 0
                else:
                    temp[num][2] += temp[i][2]
                    temp[i][2]=0
    result = 0
    for i in range(len(temp)):
        result += temp[i][2]
    print(f'#{tc} {result}')

