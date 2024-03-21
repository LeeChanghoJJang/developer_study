import sys
sys.stdin = open('input.txt')
# stack의 우선순위
isp = {'(':0,'*':2,'+':1}
# 새로 들어온 연산자의 우선순위
icp = {'(':3,'*':2,'+':1}
# 후위표기식으로 우선 변환 필요
for tc in range(1,11):
    # 이건 뭐.. 수식의 갯수인듯? 의미있나?
    N = int(input())
    # 수식은 여기에 담긴다
    equation = input()
    # 연산자를 담을 스택
    operation = []
    # 숫자를 후위표기식에 담아야겠죠?
    postfix = ''
    # 수식에서 하나씩 추출해보자고.
    for char in equation:
        # 만약 괄호가 나오거나, 아무것도 저장되지 않은 경우 무조건 추가
        # 만일 기존 스택의 연산자가 우선순위가 char보다 높으면 추가(이전꺼보다는 먼저 계산)
        if char == "(" or not operation or (char in '*+' and isp[operation[-1]] < icp[char]):
            operation.append(char)
        # char가 연산자이며, stack의 마지막보다 우선순위가 후순위 일때
        elif operation and char in '*+' and isp[operation[-1]] >= icp[char]:
            while operation and isp[operation[-1]] >= icp[char]:
                postfix += operation.pop()
            operation.append(char)
        # 닫는 괄호 나올 때! operation 있겠지만 혹시나 넣어둠
        elif operation and char == ')':
            while operation[-1] !='(':
                postfix += operation.pop()
            # 마지막 여는 괄호 빼주기
            operation.pop()
        else:
            postfix += char

    stack = []
    # 후위 표기식에서 요소 하나씩 꺼내면서 계산
    for token in postfix:
        if token in '*+':
            num1 = stack.pop()
            num2 = stack.pop()
            if token =='+':
                stack.append(int(num1)+ int(num2))
            elif token =='*':
                stack.append(int(num1)*int(num2))
        else:
            stack.append(int(token))
    print(f'#{tc} {stack.pop()}')