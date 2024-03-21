import sys
sys.stdin = open('input.txt')

for tc in range(1,int(input())+1):
    N =int(input())
    dock = sorted([list(map(int,input().split())) for _ in range(N)],key = lambda x:(x[1],x[0]))
    end = 0
    cnt = 0
    for i in range(N):
        if end <= dock[i][0]:
            end = dock[i][1]
            cnt +=1

    print(f'#{tc} {cnt}')