import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1,T+1):
    K,N,M = map(int,input().split())
    bus_station = list(map(int,input().split()))
    # 충전횟수
    cnt = 0
    # 현재위치
    loc = 0
    # 현재 위치에서 갈수 있는 거리가 도착점이 있을 때까지
    while loc + K < N:
        for step in range(K,0,-1):
            if loc + step in bus_station:
                loc += step
                cnt += 1
                break
        else:
            cnt = 0
            break

    print(f'#{tc} {cnt}')