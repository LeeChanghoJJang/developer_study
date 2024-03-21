import sys
sys.stdin = open('input.txt')

def omok(arr):
    # 세로검사
    for col in range(N):
        temp =''
        for row in range(N):
            if arr[row][col] == 'o':
                temp+='o'
            else:
                temp=''
            if temp == 'ooooo':
                return 'YES'

    # 가로검사
    for row in range(N):
        for col in range(N-4):
            if arr[row][col:col+5]=='ooooo':
                return 'YES'

    # 좌측 대각선 검사
    for alpha in range(N-4):
        for beta in range(N-4):
            temp=''
            for row in range(5):
                if arr[row+alpha][row+beta]=='o':
                    temp +='o'
                else:
                    temp = ''
            if temp == 'ooooo':
                return 'YES'

    # 우측 대각선 검사
    for alpha in range(N - 4):
        for beta in range(N - 4):
            temp = ''
            for row in range(5):
                if arr[row + alpha][4-row + beta] == 'o':
                    temp +='o'
                else:
                    temp = ''
            if temp == 'ooooo':
                return 'YES'
    return 'NO'

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [input() for _ in range(N)]
    print(f'#{tc} {omok(arr)}')


