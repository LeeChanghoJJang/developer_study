import sys
sys.stdin=open('input.txt')

def finds(N):
    cnt=0
    for i in range(1,N):
        for j in range(1,N):
            if i**2 <= N**2 - j**2:
                cnt +=1
    cnt *=4
    cnt += 4*N+1
    return cnt
for tc in range(1,int(input())+1):
    print(f'#{tc} {finds(int(input()))}')