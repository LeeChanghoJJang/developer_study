import sys
sys.stdin = open('input.txt')

def omok(y,x):
    dy = [1,0,1,-1]
    dx = [0,1,1,1]
    for bang in range(4):
        cnt = 1
        for power in range(1,5):
            ny = y + (dy[bang] * power)
            nx = x + (dx[bang] * power)
            if not (0 <= ny < n and 0 <= nx < n): break
            #돌을 발견하면  count
            if arr[ny][nx] =='o': cnt +=1
            if cnt ==5:
                return True
    return False

def game_start():
    for r in range(n):
        for c in range(n):
            if arr[r][c]=='o':
                if omok(r,c):
                    return 'YES'
    return 'NO'

T =int(input())
for tc in range(1,T+1):
    n= int(input())
    arr =[input() for _ in range(n)]
    result = game_start()
    print(f'#{tc} {result}')