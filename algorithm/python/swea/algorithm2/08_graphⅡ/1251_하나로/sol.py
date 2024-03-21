import sys
sys.stdin = open('input.txt')
'''
E : 환경부담세율
L : 해저터널 길이
환경부담금 : E * L**2

'''

for tc in range(1,int(input())+1):
    N = int(input())
    for i in range(N):
        x,y = map(int,input().split())
    E = int(input())
    print(f'#{tc} ')