import sys
sys.stdin = open('input.txt')

class Stack:
    # 입력된 길이만큼 인스턴스 생성
    def __init__(self,size):
        self.size = size
        self.data = [None] * size
        self.top = -1
    # top 위치를 증가시키고, top에 새로운 데이터 삽입
    def push(self,item):
        if self.is_full():
            print('Stack is Full!!')
        else:
            self.top += 1
            self.data[self.top] = item
    # 스택의 마지막(top)에 있는 데이터 추출
    def get(self):
        return self.data[self.top]
    # 스택의 처음부터 마지막까지 있는 데이터를 리스트 형태로 추출
    def get_all(self):
        return self.data[0:self.top+1]
    # 인스턴스 출력 시, data 원본 다 return
    def __str__(self):
        return f'{self.data}'
    # 스택이 비엇는지 안비었는지 top 이 -1이면 빈거임 그래서 push할 때 top +=1하면서 맨앞에 데이터 삽입가능
    def is_empty(self):
        return self.top ==-1
    # top이 -1이 아닐 때(안비었을때) top을 1줄이고 top에 있던 데이터 반환
    def pop(self):
        if self.is_empty():
            print('Stack is empty!!')
            return IndexError
        else:
            self.top -=1
            return self.data[self.top+1]
    # 스택의 사이즈만큼 push되어 top이 같아지면 True 반환
    def is_full(self):
        return self.size == self.top + 1

for tc in range(1, 11):
    # 주어진 패스워드의 길이를 N, 패스워드를 password라는 변수에 문자열 자료형으로 저장
    N, password = input().split()
    # stack의 인자값으로 정수를 전달하기 위해 N을 int로 변환
    N = int(N)
    stack = Stack(N)
    for char in password:
        if not stack.is_empty() and stack.get() == char:
            stack.pop()
        else:
            stack.push(char)
    print(f'#{tc} {"".join(stack.get_all())}')
    # # print(stack.__str__())