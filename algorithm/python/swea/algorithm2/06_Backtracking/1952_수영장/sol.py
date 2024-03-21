import sys
sys.stdin = open('input.txt')

def back(start,result):
    global min_val
    if start >= 12:
        if min_val > result:
            min_val = result
        return
    if min_val < result:
        return

    back(start + 1, result + plan[start]*one)
    back(start + 1, result + month)
    back(start + 3, result + quarter)
    back(start + 12, result + year)


for tc in range(1,int(input())+1):
    one, month, quarter, year = map(int,input().split())
    plan = tuple(map(int,input().split()))
    min_val = int(36001)
    back(0,0)
    print(f'#{tc} {min_val}')