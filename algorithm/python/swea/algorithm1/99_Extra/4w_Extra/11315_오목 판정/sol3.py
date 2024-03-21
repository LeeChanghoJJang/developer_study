import sys
sys.stdin = open('input.txt')
dy = [1,0,1,-1]
dx = [0,1,1,1]

def dfs(x,y):
    for i in range(4):
        cnt = 1
        for bang in range(1,5):
            nx = x + (dx[i] * bang)
            ny = y + (dy[i] * bang)
            if not (0 <= nx < N and 0<= ny < N): break
            if omok[nx][ny]=='o': cnt +=1
            if cnt == 5:
                return True
    return False

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    omok = [input() for _ in range(N)]
    result = 'NO'
    for i in range(N):
        for j in range(N):
            if omok[i][j]=='o':
                if dfs(i, j):
                    result ='YES'

    print(f'#{tc} {result}')
