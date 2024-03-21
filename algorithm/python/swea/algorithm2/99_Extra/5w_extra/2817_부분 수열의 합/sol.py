import sys
sys.stdin = open('input.txt')

def subset_sum(start,result,K):
    global cnt
    if result == K:
        cnt +=1
        return

    for next in range(start,N):
        if not visited[next]:
            visited[next] = 1
            subset_sum(next, result+arr[next], K)
            visited[next] = 0

for tc in range(1,int(input())+1):
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))
    visited = [0] * N
    cnt = 0
    subset_sum(0,0,K)
    print(f'#{tc} {cnt}')