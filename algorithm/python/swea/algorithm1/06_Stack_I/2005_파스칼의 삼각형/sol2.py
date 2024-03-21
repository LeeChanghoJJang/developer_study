import sys
sys.stdin = open('input.txt')

T= int(input())
for tc in range(1,T+1):
    N = int(input())
    print(f'#{tc}')
    for i in range(N):
        ans = str(11**i)
        print(' '.join(ans))
# 금방 오류난다..
