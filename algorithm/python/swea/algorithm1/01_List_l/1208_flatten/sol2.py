import sys
sys.stdin = open('input.txt')
for tc in range(1,11):
    cnt = int(input())
    dump = sorted(map(int,input().split()))

    while cnt:
        dump[0] +=1
        dump[-1] -=1
        dump.sort()
        cnt-=1

    print(f'#{tc} {max(dump)-min(dump)}')
