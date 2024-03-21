import sys
sys.stdin = open('input.txt')

for tc in range(1,int(input())+1):
    K,N,M = map(int,input().split())
    bus_stations = list(map(int,input().split())) + [N]
    start = 0
    cnt =0
    while start + K < N:
        for bus in bus_stations[::-1]:
            if start + K >= bus and start < bus:
                start = bus
                cnt += 1
                break
        else:
            cnt = 0
            break

    print(f'#{tc} {cnt}')
