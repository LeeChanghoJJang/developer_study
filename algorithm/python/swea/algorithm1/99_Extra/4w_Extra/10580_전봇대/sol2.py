import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    telephone_pole = sorted([list(map(int,input().split())) for i in range(N)],key = lambda x : (x[0],x[1]))
    cnt = 0
    for start in range(N-1):
        for now in range(start+1,N):
            if telephone_pole[start][1] > telephone_pole[now][1]:
                cnt +=1
    print(f'#{tc} {cnt}')