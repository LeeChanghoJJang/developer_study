import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    bus = [0]*5001
    for i in range(N):
        A,B = map(int, input().split())
        for stop in range(A,B+1):
            bus[stop] +=1
    P = int(input())
    bus_stations = []
    for i in range(P):
        C = int(input())
        bus_stations.append(bus[C])
    print(f'#{tc}', ' '.join(map(str,bus_stations)))
# 강사님 풀이
for tc in range(1,T+1):
    N = int(input())
    counts = [0]*5001
    for i in range(N):
        A,B = map(int,input().split())
        for j in range(A,B+1): # 1<=A,B<=5000
            counts[j]+=1
    P = int(input())
    busstop = [int(input()) for _ in range(P)]
    print(f'#{tc} end=' ')
    for i in busstop:
        print(counts[i],end=' ')