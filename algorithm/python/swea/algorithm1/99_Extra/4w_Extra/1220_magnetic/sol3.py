import sys
sys.stdin = open('input.txt')

def Magnetic(arr):
    result = 0
    for col in range(N):
        cnt = 0
        for row in range(N):
            if not cnt and arr[row][col] == 1:
                cnt = 1
            elif cnt and arr[row][col] == 2:
                cnt = 0
                result +=1
    return result

for tc in range(1,11):
    N= int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    print(f'#{tc} {Magnetic(arr)}')