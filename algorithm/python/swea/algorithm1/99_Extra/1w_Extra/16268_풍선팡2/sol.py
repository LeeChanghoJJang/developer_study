import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1,T+1):
    N,M = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]
    # (1,1)부터 (N-2,M-2) 까지가 가운데여야 함
    max_sum = 0
    for row in range(1,N-1):
        for col in range(1,M-1):
            nearby = sum(arr[row][col-1:col+2]+arr[row-1][col:col+1]+arr[row+1][col:col+1])
            if nearby >= max_sum:
                max_sum = nearby
    print(f'#{tc} {max_sum}')
# 강사님 풀이
di = [0,1,0,-1]
dj = [1,0,-1,0]
T = int(input())
for tc in range(1,T+1):
    N,M = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]
    max_v =0 # 최대 꽃가루의 합계
    for i in range(N): # N x M 크기의 게임판
        for j in range(M):
            cnt = arr[i][j] # 터뜨린 풍선의 꽃가루 수
            # 주변 풍선의 꽃가루
            for k in range(4):
                ni = i +di[k]
                nj = j +dj[k]
                if 0 <=ni < N and 0<=nj<M:
                    cnt += arr[ni][nj]
            # 꽃가루를 최대값과 비교
            if max_v < cnt:
                max_v =cnt
    print(f'#{tc} {max_v}')