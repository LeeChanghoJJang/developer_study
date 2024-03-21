import sys
from collections import deque
sys.stdin = open('input.txt')
# BFS 함수 설정
def BFS(S,G):
    # 초기값을 queue에 저장
    queue = deque([S])
    # queue에 원소가 있는 동안만(탐색 안한게 없을 때까지)
    while queue:
        now = queue.popleft()
        # 나온 값이 G면 바로 함수 종료하고 누적된 거리값 반환
        if now == G:
            return visited[now]
        # arr에서 next값 추출
        for next in arr[now]:
            # 연결된 길이 있는지 순회
            if visited[next]==0:
                # 다음 탐색한 길로 이동할 때마다 기존 거리에 +1
                visited[next] = visited[now]+1
                # queue에 원소를 넣어 다음 탐색 ㄱㄱ
                queue.append(next)
    return 0

T = int(input())
for tc in range(1,T+1):
    V,E = map(int,input().split())
    arr = [[] for _ in range(V+1)]
    visited = [0] * (V+1)
    # 연결정보만큼 순회하여 인접리스트 저장장    for i in range(E):
        start, arrive = map(int,input().split())
        arr[start].append(arrive)
        arr[arrive].append(start)
    S,G = map(int,input().split())
    print(f'#{tc} {BFS(S,G)}')

