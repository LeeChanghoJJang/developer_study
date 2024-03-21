import sys
sys.stdin = open('input.txt')

for tc in range(1,int(input())+1):
    N = int(input())
    X = int(N ** (1/3))
    for j in (X, X+1):
        if j**3 == N:
            print(f'#{tc} {j}')
            break
    else:
        print(f'#{tc} -1')
