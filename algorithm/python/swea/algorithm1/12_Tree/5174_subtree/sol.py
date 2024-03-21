import sys
sys.stdin = open('input.txt')

def pre_order(T):
    global cnt
    if T:
        # print(T,end=' ')
        cnt +=1
        pre_order(left[T])
        pre_order(right[T])

T = int(input())
for tc in range(1,T+1):
    E,N = map(int,input().split())
    arr = list(map(int,input().split()))
    # 좌우측 노드 저장
    left = [0] * (E+2)
    right = [0] * (E+2)

    for i in range(E):
        p,c = arr[i*2],arr[i*2+1]
        # 부모의 왼쪽 자식이 없으면 왼쪽자식에 저장
        if left[p] ==0:
            left[p]=c
        # 부모의 왼쪽자식 있으면 오른쪽 자식에 저장
        else:
            right[p]=c
        # 자식노드 인덱스에 부모 노드 저장
    cnt = 0
    pre_order(N)
    print(f'#{tc} {cnt}')
