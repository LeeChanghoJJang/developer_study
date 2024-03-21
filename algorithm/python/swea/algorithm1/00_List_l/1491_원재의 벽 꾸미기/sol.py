import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1,T+1):
    N,A,B = map(int,input().split())
    # A * abs(R-C) + B * (N - R*C)
    # A는 최대한 정사각형, B는 최대한 타일 다사용
    # N개의 타일을 통해  R *C 크기의 직사각형 만들고자 함
    # R과 C를 어떻게 순회할 것인가?
    min_num = float('inf')
    # N에서 순차적으로 number를 착출 (N, N-1, N-2, ..., 1)
    for number in range(N,int(N**0.5)**2-2,-1):
        escape = False
        # number를 R로 나누었을 때 가능한 수 추출
        for R in range(1, int(number**0.5)+1):
            if number % R == 0:
                C = number // R
                if A * abs(R-C) + B * (N - R*C) ==0:
                    min_num = 0
                    escape = True
                    break
                if min_num > A * abs(R-C) + B * (N - R*C):
                    min_num = A * abs(R-C) + B * (N - R*C)
        if escape:
            break
    print(f'#{tc} {min_num}')