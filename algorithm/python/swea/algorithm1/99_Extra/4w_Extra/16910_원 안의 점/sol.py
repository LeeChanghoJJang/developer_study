import sys
sys.stdin =open('input.txt')

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    result = 0
    for i in range(N-1,0,-1):
        for j in range(N-1,0,-1):
            if i **2 + j**2 <= N**2:
                result += i
                break
    result *=4
    result += 4*N+1
    print(f'#{tc} {result}')