import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1,T+1):
    cnt = 0
    stick = input()
    # stack =[]
    result = 0

    for i in range(len(stick)):
        if stick[i] =='(':
            cnt +=1
        elif stick[i] ==')':
            cnt -=1
            if stick[i-1] =='(':
                result +=cnt
            elif stick[i-1] ==')':
                result +=1
    print(f'#{tc} {result}')


# while stick:
    #     bracket = stick.pop(0)
    #     # 벽 쌓을 때
    #     if bracket =='(':
    #         cnt+=1
    #     # 막대기 최종 길이 확정 또는 레이저 확정
    #     elif bracket ==')':
    #         # 기존에 추가했던 (를 -시켜 원상복구
    #         cnt -= 1
    #         # 레이저인 경우에는 result에 이전에 자른 막대기들 추가
    #         if stack[-1] =='(':
    #             result += cnt
    #         # 각 막대기들 잘릴 때마다 하나씩 result값 추가
    #         elif stack[-1] ==')':
    #             result +=1
    #     # 괄호는 지속적으로 추가
    #     stack.append(bracket)

