import sys
sys.stdin = open('input.txt')

def max_money(now, cnt,number):
    global result
    if now == cnt:
        numbers = ''.join(number)
        if result < int(numbers):
            result = int(numbers)
        return

    if (now, tuple(number)) in visited:
        return
    visited.add((now, tuple(number)))

    for k in range(len(number)):
        for next in range(len(number)):
            if k != next:
                number[k], number[next] = number[next], number[k]
                max_money(now+1,cnt,number)
                number[k], number[next] = number[next], number[k]

for tc in range(1,int(input())+1):
    number, cnt = input().split()
    number = list(number)
    cnt = int(cnt)
    visited = set()
    result = 0
    max_money(0,cnt,number)
    print(f'#{tc} {result}')
