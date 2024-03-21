import sys
sys.stdin = open('input.txt')
from collections import deque
T = int(input())
for tc in range(1,T+1):
    N,M = map(int,input().split())
    # 피자의 번호를 반환하기 위해 enumerate를 포함하여 리스트 만듦
    pizza = list(enumerate(map(int,input().split()),start=1))
    # 화덕에 놓여질 피자를 피자 리스트에서 추출
    fire_pit = deque(pizza[:N])
    # 남은 피자를 피자변수에 저장
    pizza = pizza[N:]
    # 화덕에서 0이 되는 피자 추출
    while len(fire_pit) > 1:
        # 첫번째 위치 pizza를 first_pizza라고 명명하며, 젤 왼쪽에서 추출
        first_pizza = fire_pit.popleft()
        # 피자의 치즈가 반으로 줄었을 때 양을 갱신하기 위해 리스트로 자료형 변환
        first_pizza = list(first_pizza)
        # 맨첨에 꺼냈을 때, 치즈의 양 반으로 저장
        first_pizza[1]//=2
        # 만약 치즈가 다 녹지 않았으면, 화덕 맨 뒷칸으로 이동
        if first_pizza[1] != 0:
            fire_pit.append(first_pizza)
        # 피자가 여분이 있으면서 first_pizza의 치즈가 다녹으면 화덕에 추가
        elif pizza:
            fire_pit.append(pizza.pop(0))

    print(f'#{tc} {fire_pit[0][0]}')