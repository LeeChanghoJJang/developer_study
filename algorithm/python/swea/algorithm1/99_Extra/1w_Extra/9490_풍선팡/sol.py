import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    balloon =[]
    for _ in range(N):
        balloon.append(list(map(int, input().split())))
    temp =[]
    for row in range(N):
        for col in range(M):
            sum_max = balloon[row][col]
            k=balloon[row][col]
            while k > 0:
                if row + k < N:
                    sum_max += balloon[row + k][col]
                if row - k >= 0:
                    sum_max += balloon[row - k][col]
                if col + k < M:
                    sum_max += balloon[row][col + k]
                if col - k >= 0:
                    sum_max += balloon[row][col - k]
                k-=1
            temp.append(sum_max)
    print(f'#{tc} {max(temp)}')
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
                for l in range(1,arr[i][j]+1):
                    ni = i +di[k]*l
                    nj = j +dj[k]*l
                    if 0 <=ni < N and 0<=nj<M:
                        cnt += arr[ni][nj]
            # 꽃가루를 최대값과 비교
            if max_v < cnt:
                max_v =cnt
    print(f'#{tc} {max_v}')