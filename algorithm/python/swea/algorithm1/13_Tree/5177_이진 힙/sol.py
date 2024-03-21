import sys
sys.stdin = open('input.txt')

def enq(n):
    global last
    last += 1 # 마지막 노드 뒤에 삽입 (완전 이진트리 유지)
    heaps[last] = n # 마지막 노드에 데이터 삽입
    son = last # 부모 > 자식 비교
    parents = son//2 # 부모번호 계산
    # 부모노드가 1보다 클때, 부모노드가 자식노드값보다 클때!
    while parents >= 1 and heaps[parents] > heaps[son]:
        # 부모가 크면 안되니까 자식과 교환
        heaps[parents], heaps[son] = heaps[son], heaps[parents]
        # 조상님들도 크면 안되니까 교환기회를 드리기 위해 son을 parents로 갱신
        son = parents
        # 부모님들은 조상님으로 변경
        parents = son//2

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    heaps = [0] * (N+1)
    last = 0
    inputs = list(map(int, input().split()))
    # 각 인풋마다 값을 저장하고, 최소값을 조상님과 변경하는 작업 실시
    for a in inputs:
        enq(a)
    result = 0
    # 최종노드의 부모노드만 합을 도출
    while N > 1:
        N//=2
        result +=heaps[N]
    print(heaps)
    print(f'#{tc} {result}')