import sys
sys.stdin = open('input.txt')

def prime_number(switch,number):
    temp = []
    prime = [0] * (switch+1)
    for i in range(2,switch+1):
        cnt= 0
        for j in range(1,switch+1):
            if i%j == 0:
                cnt += 1
        if cnt == 2:
            temp.append(i)
    for idx in temp:
        n = number
        state[idx] = 1 - state[idx]
        while n:
            if idx + n < switch:
                state[idx + n] = 1 - state[idx + n]
            if idx - n > 0:
                state[idx - n] = 1 - state[idx - n]
            n-=1

def measure(num):
    for i in range(1,num+1):
        if num % i == 0:
            state[i] = 1 - state[i]

T = int(input())

for tc in range(1,T+1):
    switch = int(input())
    state = [0] + list(map(int,input().split()))
    student = int(input())
    for i in range(student):
        gender, number = map(int,input().split())
        if gender==1:
            prime_number(switch,number)
        elif gender ==2:
            measure(number)
    print(f'#{tc}',end=' ')
    print(*state[1:])