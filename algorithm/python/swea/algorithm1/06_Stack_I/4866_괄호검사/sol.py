import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1,T+1):
    word = input()
    stack =[]
    cnt=1
    for char in word:
        if char in ['(','{']:
            stack.append(char)
        elif stack and ((char==')' and stack[-1] =='(') or (char=='}' and stack[-1] =='{')):
            stack.pop()
        elif char in [')','}']:
            cnt=0
            break

    if len(stack) !=0:
        cnt=0
    print(f'#{tc} {cnt}')