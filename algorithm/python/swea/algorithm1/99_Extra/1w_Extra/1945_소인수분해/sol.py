import sys
sys.stdin = open('input.txt')

T = int(input())
divided = [2,3,5,7,11]
for tc in range(1,T+1):
    exponent = []
    N =int(input())
    for i in divided:
        cnt=0
        while N%i ==0:
            N//=i
            cnt +=1
        exponent.append(cnt)

    print(f'#{tc}',end=' ')
    print(*exponent)