import sys
sys.stdin = open('input.txt')

def insecticide(i,j,M):
    result = 0
    up_limit_i = min(i + M, N)
    up_limit_j = min(j + M, N)
    for x in range(i,up_limit_i):
        for y in range(j,up_limit_j):
            if x in [i,i+M-1] or y in [j,j+M-1]:
                result += flies[x][y]
    return result

def search(flies):
    max_val = 0
    for i in range(N):
        for j in range(N):
            if max_val < insecticide(i,j,M):
                max_val = insecticide(i,j,M)
    return max_val

T = int(input())
for tc in range(1,T+1):
    N,M = map(int,input().split())
    flies = [list(map(int,input().split())) for _ in range(N)]
    print(f'#{tc} {search(flies)}')