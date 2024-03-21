import sys
sys.stdin =open('input.txt')

def magnetic(arr):
    global cnt
    for col in range(N):
        temp = []
        for row in range(N):
            if not temp and arr[row][col] == '1':
                temp.append(arr[row][col])
            elif temp and arr[row][col] == '2':
                cnt += 1
                temp.pop()
    return cnt


for tc in range(1,11):
    N = int(input())
    arr = [input().split() for _ in range(N)]
    cnt = 0
    print(f'#{tc} {magnetic(arr)}')