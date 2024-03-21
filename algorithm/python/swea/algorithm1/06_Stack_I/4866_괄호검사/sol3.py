import sys
sys.stdin = open('input.txt')

T = int(input())

for test in range(1, T+1):
    top = -1
    bracket = input()
    stack = []
    for n in bracket:  # data를 하나씩 순회하면서
        if n == '(' or n == '{':   # 해당 문자가 여는 괄호라면
            top += 1
            stack.append(n)  # 해당 data를 넣어줌
        elif n == ')':  # 해당 문자가 닫는 소괄호라면
            if not stack: # stack 리스트가 비어있으면
                top += 1
                stack.append(n)
            elif stack and stack[top] == '(': # stack에 뭐가 있고 소괄호 짝이 맞을 경우
                top -= 1
                stack.pop()
        elif n == '}':  # 해당 문자가 닫는 소괄호라면
            if not stack:  # stack 리스트가 비어있으면
                top += 1
                stack.append(n)
            elif stack and stack[top] == '{':  # stack에 뭐가 있고 중괄호 짝이 맞을 경우
                top -= 1
                stack.pop()
        else:   # 해당 문자가 괄호들이 아니라면
            continue

    if stack:  # stack 리스트에 뭐가 남아있으면
        result = 0
    else:   # stack 리스트가 비어있으면
        result = 1
    # print(stack)

    print(f'#{test} {result}')