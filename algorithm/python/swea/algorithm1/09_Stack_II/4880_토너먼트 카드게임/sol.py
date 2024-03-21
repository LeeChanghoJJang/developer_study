import sys
sys.stdin = open('input.txt')

def rock_paper_scissors(a,b):
    # 각 인덱스에 해당되는 값으로 가위바위보 비교
    if abs(cards[a] - cards[b]) == 1:
        if cards[a] > cards[b]:
            return a
        else:
            return b

    elif abs(cards[a] - cards[b]) == 2:
        if cards[a] > cards[b]:
            return b
        else:
            return a
    else:
        return a

# 결과적으로 인덱스를 반환하는 게 목표이므로, 각 인덱스값을 파라미터로 설정
def divide_conquer(i,j):
    print(i,j)
    # 본인 자신과 같은 경우 // 혼자밖에 없는 경우
    if i == j:
        return i
    else: # 한 개가 아닌 경우에는 무조건 분할
        front = divide_conquer(i, (i + j) // 2)
        rear = divide_conquer((i + j) // 2+1, j)
        return rock_paper_scissors(front,rear)
'''
ex) N= 3이면
맨처음에 divide_conquer(0,3) 넣으면
front = divide_conquer(0,1)
rear = divide_conquer(2,3)
--------------------------
front에 저장된 divide_conquer(0,1)도 계산하기 위해 재귀함수 들어가보면
front = divide_conquer(0,0) = 0
rear = divide_conquer(1,1) = 1
rock_paper_scissors(front,rear) 계산하면 이긴쪽의 인덱스가 반환됨
divide_conquer(0,1) = 방금 위의 front, rear에서 이긴것 
'''

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    cards = list(map(int,input().split()))
    print(f'#{tc} {divide_conquer(0,N-1)+1}')