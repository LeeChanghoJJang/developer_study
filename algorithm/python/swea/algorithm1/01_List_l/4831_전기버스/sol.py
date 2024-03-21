import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1,T+1):
    K, N, M = map(int,input().split())
    stations = list(map(int, input().split()))
    # 최대로 갈 수 있는 거리 내에서 갈지 말지 결정하기
    # 출발점
    start= 0
    # 충전 횟수
    cnt= 0
    # 갈수 있는 최대 거리
    can_go = start + K
    # 현재 위치와 다른 위치를 비교하기 위한 location 지정
    location = 0
    # 최대로 갈 수 있는 거리 안에 N이 들어오면 반복문 종료
    while can_go < N:
        # location이 마지막 정류장일 때, stations 내 정류장이 아닌 N과 비교
        if location == M-1:
            # 마지막 정류장에서의 start와 can_go(최대 갈수 있는거리) 갱신
            start = stations[location]
            can_go = start +K
            if N <= can_go: # 최대 갈 수 있는 범위면 충전 횟수 추가
                cnt +=1
            else: # 최대 갈 수 없는 거리면 충전 횟수 리셋
                cnt = 0
                break
        # 다음 location 한번에 갈 수 있는 범위고, 그 다음 location이 한번에 갈 수 없는 범위인지 확인
        elif stations[location] <= can_go and stations[location+1] > can_go:
            # 이러한 경우 정류장에서 충전 한번
            cnt += 1
            # 여기서 재출발
            start = stations[location]
            # 출발지점이 달라지고 완충함에 따라 갈 수 있는 최대거리 재지정
            can_go = start + K
        # 만약 다음 정류장을 한 번에 갈 수 없는 범위라면
        elif can_go < stations[location]:
            # 여태까지 온것이 말짱 꽝이므로, 충전횟수를 리셋한 후, 반복문 break
            cnt = 0
            break
        # 매번 다음 정류장으로 이동하고, 충전여부를 비교하기 위해 위치 1씩 향상
        location +=1

    print(f'#{tc} {cnt}')