import sys
sys.stdin = open('input.txt')

def arr_min_sum(start,result):
    global min_val
    if start == N:
        if result < min_val:
            min_val = result
        return

    for col in range(N):
        if visited[col] < 2 and result+arr[start][col] < min_val:
            visited[col] += 1
            arr_min_sum(start+1,result+arr[start][col])
            visited[col] -= 1

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    min_val = float('inf')
    arr = [list(map(int,input().split())) for _ in range(N)]
    visited = [0] * N
    arr_min_sum(0,0)
    print(f'#{tc} {min_val}')