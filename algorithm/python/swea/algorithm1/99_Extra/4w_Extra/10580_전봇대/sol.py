import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    telephone_pole = sorted([list(map(int,input().split())) for _  in range(N)],key = lambda x:(x[0],x[1]))
    cnt=0
    for start in range(N-1):
        for next in range(start,N):
            # 시작점 순차인데, 끝점 마저 앞놈보다 작으면 겹친거 인정
            if telephone_pole[start][1] > telephone_pole[next][1]:
                cnt +=1

    print(f'#{tc} {cnt}')