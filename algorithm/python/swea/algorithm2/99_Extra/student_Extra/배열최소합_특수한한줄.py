import sys
sys.stdin = open('input.txt')

def arr_min_sum(start,result):
    global min_val
    if start == N:
        if min_val > result:
            min_val = result
        return

    for i in range(N):
        if start in special and result + arr[start][i] < min_val :
            arr_min_sum(start + 1, result + arr[start][i])

        elif not visited[i] and result + arr[start][i] < min_val:
            visited[i]=1
            arr_min_sum(start+1,result + arr[start][i])
            visited[i]=0

T = int(input())
for tc in range(1,T+1):
    min_val = float('inf')
    N,M = map(int,input().split())
    special = list(map(lambda x : int(x)-1,input().split()))
    arr = [list(map(int,input().split())) for _  in range(N)]
    visited = [0] * N
    arr_min_sum(0,0)
    print(f'#{tc} {min_val}')
