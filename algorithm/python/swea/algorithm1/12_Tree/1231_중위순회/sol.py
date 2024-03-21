import sys
sys.stdin = open('input.txt')


def inorder(now):
    # 왼쪽 자식노드의 now가 0일떄
    if now != 0:
        inorder(trees[now][0])
        print(alphabet[now],end='')
        inorder(trees[now][1])

for tc in range(1,11):
    N = int(input())
    trees = [[0,0] for _ in range(N+1)]
    alphabet = [0] * (N+1)
    for i in range(N):
        # 문제에서 주어진 조건 저장
        node, alpha, *direction = input().split()
        alphabet[int(node)] = alpha
        # 왼쪽 오른쪽 자식노드가 2일 때
        if len(direction) ==2 :
            trees[int(node)][0] = int(direction[0])
            trees[int(node)][1] = int(direction[1])
        # 왼쪽 오른쪽 자식노드가 1일 때
        elif len(direction) == 1:
            trees[int(node)][0] = int(direction[0])
    print(f'#{tc}',end=' ')
    inorder(1)
    print()