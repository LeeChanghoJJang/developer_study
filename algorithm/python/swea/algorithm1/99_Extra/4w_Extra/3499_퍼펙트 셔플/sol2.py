import sys
sys.stdin = open('input.txt')

for tc in range(1,int(input())+1):
    N = int(input())
    alphabet = tuple(input().split())
    if N%2: arange = N//2+1
    else: arange = N//2
    print(f'#{tc}',end=' ')
    for i in range(arange):
        if N%2 and i == N//2:
            print(alphabet[i],end=' ')
        else:
            print(alphabet[i],alphabet[i+arange],end=' ')
    print()