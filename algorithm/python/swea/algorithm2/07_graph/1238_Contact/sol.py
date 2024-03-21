import sys
from collections import deque
# 입력 파일을 표준 입력으로 변경
sys.stdin = open('input.txt')


# BFS 함수 정의
def BFS(start):
    # 시작 노드를 큐에 추가
    queue = deque([start])
    # 각 노드의 순위를 저장할 리스트 초기화
    rank = [0] * 101
    # 시작 노드 방문 표시
    visit[start] = 1

    # BFS 탐색 시작
    while queue:
        now = queue.popleft()  # 큐에서 노드를 꺼냄
        for next in graph[now]:  # 현재 노드의 이웃 노드들을 확인
            if not visit[next]:  # 이웃 노드가 방문되지 않았을 경우
                visit[next] = 1  # 방문 표시
                queue.append(next)  # 큐에 추가
                rank[next] = rank[now] + 1  # 현재 노드의 순위에서 1을 더한 값을 이웃 노드의 순위로 설정

    # 가장 먼 노드의 순위를 찾음
    max_val = max(rank)
    temp = 0
    for i in range(1, 101):
        if rank[i] == max_val:
            temp = i  # 가장 먼 노드를 찾음

    return temp


# 메인 함수
for tc in range(1, 11):  # 총 10개의 테스트 케이스에 대해 반복
    graph = [[] for _ in range(101)]  # 그래프 초기화
    N, start = map(int, input().split())  # 노드의 개수와 시작 노드 입력
    arr = list(map(int, input().split()))  # 간선 정보 입력
    visit = [0] * 101  # 방문 여부를 저장할 리스트 초기화

    # 그래프 정보 생성
    for i in range(1, N, 2):
        graph[arr[i - 1]].append(arr[i])

    # BFS를 이용하여 가장 먼 노드를 찾고 결과 출력
    print(f'#{tc} {BFS(start)}')
