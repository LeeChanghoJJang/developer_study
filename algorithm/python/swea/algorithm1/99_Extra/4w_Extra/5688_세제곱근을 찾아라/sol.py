import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    cnt = 0
    for i in range(2):
        if (int(N**(1/3))+i)**3 == N:
            cnt = int(N**(1/3))+i
            break
        else:
            cnt = -1
    print(f'#{tc} {cnt}')