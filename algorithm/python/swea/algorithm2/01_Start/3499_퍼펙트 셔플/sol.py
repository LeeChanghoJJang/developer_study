import sys
sys.stdin = open('input.txt')

# 투 포인트 알고리즘 이용
for tc in range(1,int(input())+1):
    N = int(input())
    words = input().split()
    a= 0
    b= int((N+1)/2)
    print(f'#{tc}',end=' ')
    while a < int((N+1)/2):
        if N%2 ==1 and a==int((N+1)/2)-1:
            print(words[a],end=' ')
        else:
            print(words[a],words[b], end=' ')
        a+=1; b+=1
    print()
