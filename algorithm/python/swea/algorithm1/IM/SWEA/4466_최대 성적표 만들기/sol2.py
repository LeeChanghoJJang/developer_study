import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1,T+1):
    N,K = map(int,input().split())
    score = sorted(map(int,input().split()))
    result = 0
    while K>0:
        temp = score.pop()
        result +=temp
        K-=1
    print(f'#{tc} {result}')