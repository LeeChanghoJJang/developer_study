import sys
sys.stdin = open('input.txt')


def fibonaci(n):
    global cnt_0
    global cnt_1
    if n ==0:
        cnt_0 +=1
        return dic[0]

    elif n==1:
        cnt_1 +=1
        return dic[1]

    dic[n] = fibonaci(n - 1) + fibonaci(n - 2)
    return dic[n]

dic = {0: 0, 1: 1}

T = int(input())

for _ in range(T):
    cnt_0 = 0
    cnt_1 = 0
    N = int(input())
    fibonaci(N)
    print(cnt_0, cnt_1)
