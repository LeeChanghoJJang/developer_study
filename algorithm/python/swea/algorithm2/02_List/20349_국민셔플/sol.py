import sys
sys.stdin = open('input.txt')

for tc in range(1,int(input())+1):
    N,T = map(int,input().split())
    overhand_portion = int(N*0.37)
    cards = list(range(1,N+1))
    cnt = 0
    while cnt < T:
        cnt +=1
        cards = cards[N-overhand_portion:] + cards[:N-overhand_portion]
        temp = []
        a = 0
        b = int((N+1)/2)
        c = 0
        while len(temp) < N:
            if c%2 ==0:
                temp.append(cards[a])
                a += 1
            elif c%2 ==1:
                temp.append(cards[b])
                b += 1
            c+=1
        cards = temp
    print(f'#{tc}',end=' ')
    print(*cards)
