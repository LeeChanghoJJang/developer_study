import sys
sys.stdin = open('input.txt')

def find_five(arr,N):
    # 가로검사
    for x in range(N):
        for y in range(N-5+1):
            if arr[x][y:y+5] =='ooooo':
                return 'YES'
    # 세로검사
    for y in range(N):
        temp = ''
        for x in range(N):
            if arr[x][y] =='o':
                temp += arr[x][y]
            else:
                temp =''
            if temp =='ooooo':
                return 'YES'

    # 대각선 검사
    cnt = 0
    for beta in range(N-5+1):
        for alpha in range(N-5+1):
            for x in range(5):
                if arr[x+beta][x+alpha] =='o':
                    cnt +=1
                else:
                    cnt = 0
            if cnt==5:
                return 'YES'

    # 대각선 검사
    cnt = 0
    for beta in range(N - 5 + 1):
        for alpha in range(N - 5 + 1):
            for x in range(5):
                if arr[x + beta][4 - x + alpha] == 'o':
                    cnt += 1
                else:
                    cnt = 0
            if cnt == 5:
                return 'YES'
    return 'NO'

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    omok = [input() for _ in range(N)]
    print(f'#{tc} {find_five(omok,N)}')