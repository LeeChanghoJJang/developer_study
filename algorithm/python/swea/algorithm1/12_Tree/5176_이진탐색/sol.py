import sys
sys.stdin = open('input.txt')

# 하나의 부모노드를 호출했을 때, 조건을 충족하면 두개의 자식 노드를 호출하는 함수
# 재귀 함수 호출하는 것이랑 트리의 구조랑 매우 흡사함
def inorder(now):
    global cnt
    # 만약 호출했는데 now가 N보다 크면 더이상 자식노드 조건을 충족하지 않음
    if now <= N:
        # 좌측 자식노드 호출
        inorder(now * 2)
        # 순서대로 cnt를 증가시켜서 값을 저장
        cnt += 1
        # trees에 현재 노드의 cnt를 저장
        trees[now] = cnt
        print(trees, now)
        # 우측 자식노드 호출
        inorder(now * 2 + 1)
        # 끝나면 부모노드로 회귀

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    trees = [0] * (N+1)
    # trees에 값을 저장하기 위한 cnt 저장
    cnt = 0
    # 1번 정점부터 시작
    inorder(1)
    print(f"#{tc} {trees[1]} {trees[N//2]}")











