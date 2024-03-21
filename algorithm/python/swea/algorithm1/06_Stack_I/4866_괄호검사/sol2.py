import sys
sys.stdin = open('input1.txt')

class Stack:
    # stack을 생성할 때 필요한 값이 있는데,
    # stack의 크기를 지정해야 한다.
    def __init__(self,size):
        self.size = size
        # 자료구조 stack을 list를 활용해서 구현
        self.data = [None] * size #값이 없음을 나타내는 None
        self.top = -1

    def push(self,item): # stack에 값 삽입 -> 삽입할 대상 item을 인자로 받는다.
        # stack이 가득 찼다면
        if self.is_full():
            print('Stack is Full!!')
        else:
            self.top +=1
            # 받아온 item을 내 data에 top번째 위치에 삽입
            self.data[self.top] = item

    def get(self):
        return self.data[self.top]

    def __str__(self): # instance print했을 때, stack 안의 data 바로 출력
        return f'{self.data}'

    def is_empty(self):
        # top이 -1을 가리키고 있다면 stack은 비었다.
        return self.top == -1

    def pop(self):
        if self.is_empty():
            print('Stack is empty!!')
            return IndexError
        else:
            self.top -=1
            return self.data[self.top+1]

    def is_full(self):
        return self.size == self.top +1

T = int(input())

for tc in range(1,T+1):
    bracket = input()
    stack = Stack(100)
    # 모든 문자열을 조사
    result = True
    for char in bracket:
        if char =='(':
            stack.push(char)
        elif char ==')':
            if not stack.is_empty():
                stack.pop()
            else:
                result = False
                break
    if not stack.is_empty():
        result = False

    print(f'#{tc} {result}')