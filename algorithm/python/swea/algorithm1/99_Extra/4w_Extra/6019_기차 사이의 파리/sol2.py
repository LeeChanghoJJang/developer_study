import sys
sys.stdin = open('input.txt')

for tc in range(1,int(input())+1):
    D,A,B,F = map(int,input().split())
    print(f'#{tc} {D/(A+B)*F}')