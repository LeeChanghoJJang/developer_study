import sys
sys.stdin = open('input.txt')
T = int(input())
# 계산하기 함수
def evaluate(a,b,i):
    a= int(a)
    b= int(b)
    if i=='*':
        return a*b
    elif i=='+':
        return a+b
    elif i=='-':
        return a-b
    elif i=='/' or i=='//':
        return a//b

for tc in range(1,T+1):
    # 수식을 operation으로 지정
    operation = input().split()
    # 중간 계산값이나 숫자를 저장할 스택 temp 설정
    temp = []
    # 최종 결과값 저장을 위한 result 설정
    result=''
    # 수식을 반복문 순회
    for i in operation:
        # 숫자가 나올 경우에는 임시스택에 추가
        if i.isdigit():
            temp.append(i)
        # 숫자가 아닐 경우에는 아래와 같이 처리
        elif not i.isdigit():
            # 온점 나오면 연산 끝이므로 break
            if i =='.':
                break
            # 숫자가 두 개 이상되어야 연산이 가능하므로, 리스트의 원소를 꺼내어 계산하고, 다시 스택에 가산
            elif len(temp) >= 2:
                end = temp.pop()
                front = temp.pop()
                temp.append(evaluate(front,end,i))
            # 숫자가 한 개인데 연산자가 나온 경우, 연산이 불가하므로 error를 result에 저장
            elif len(temp) < 2:
                result='error'
                break
    # 만약 위의 반복문을 순회했을 때, 최종 숫자가 1개만 나온 경우에는 result에 temp의 계산 결과를 저장
    if len(temp)==1 and result !='error':
        result = temp[0]
    # 혹시나 temp에 최종 숫자가 2개일 때에도, 전부 계산된 게 아니기 때문에 error를 result에 저장
    elif len(temp)>=2:
        result = 'error'
    print(f'#{tc} {result}')
