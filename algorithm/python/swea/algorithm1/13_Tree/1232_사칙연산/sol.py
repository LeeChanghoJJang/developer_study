import sys
sys.stdin = open('input.txt')

# 계산하기 : +*/-에 따라서
def calculate(operation,num1,num2):
    if operation=='+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        return num1 / num2
# 연산을 해서 부모노드로 이송하는 작업
def operation(idx):
    # 연산자, 숫자 2개가 주어진 경우
    if len(trees[idx]) ==3:
        oper, num1, num2 = trees[idx]
        # 위 num1,num2 숫자들은 인덱스에 해당 되는 값을 호출하기 위해 재귀함수 사용
        # 또 길이가 3이면 또 호출하겠지..하지만 언젠가 답은 나온다.
        return calculate(oper,operation(int(num1)),operation(int(num2)))
    # 숫자 하나만 주어진 경우에는 숫자만 반환
    elif len(trees[idx])==1:
        return int(trees[idx][0])

for tc in range(1,11):
    N = int(input())
    trees = [[] for _ in range(N+1)]
    for i in range(N):
        idx, *etc = input().split()
        # 기존에 []으로 저장되있어, append를 하면 이중 리스트 형태가 되어 extend 사용
        trees[int(idx)].extend(etc)
    # 결과값은 정수값으로 출력해라고 함
    print(f'#{tc} {round(operation(1))}')