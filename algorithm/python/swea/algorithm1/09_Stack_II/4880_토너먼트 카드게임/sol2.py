import sys
sys.stdin = open('input.txt')

def rock_scissors_paper(start,end):
    if (start + 1) % 3 < (end+1) %3:

1 <2 <3 <1
def tonaments(arr):
    if len(arr) == 1:
        return arr
    elif len(arr) >= 2:
        start = tonaments(arr[:len(arr)//2])
        end = tonaments(arr[:len(arr) // 2])
        return rock_scissors_paper(start,end)

for tc in range(1,int(input())+1):
    N = int(input())
    cards = list(map(int,input().split()))
    tonaments
    print(f'#{tc} ')
