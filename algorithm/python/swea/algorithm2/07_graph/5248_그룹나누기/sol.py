import sys

# 입력 파일을 표준 입력으로 변경
sys.stdin = open('input.txt')

def union_graph(arr):
    # 그래프 초기화
    graph = [[] for _ in range(N + 1)]
    # 방문 여부를 저장할 리스트 초기화
    visited = [0] * (N + 1)
    # 간선의 개수
    n = len(arr)
    # 연결된 요소의 개수를 저장할 변수 초기화
    cnt = 0
    # 그래프 생성
    for i in range(0, n, 2):
        graph[arr[i]].append(arr[i + 1])
        graph[arr[i + 1]].append(arr[i])

    # DFS를 이용하여 연결된 요소의 개수를 찾음
    for start in range(1, N + 1):
        if not visited[start]:
            stack = [start]
            while stack:
                now = stack.pop()
                visited[start] = 1
                for next in graph[now]:
                    if not visited[next]:
                        visited[next] = 1
                        stack.append(next)
            cnt += 1  # 연결된 요소의 개수 증가
    return cnt


# 메인 함수
for tc in range(1, int(input()) + 1):
    # 노드의 개수(N)와 간선의 개수(M) 입력
    N, M = map(int, input().split())
    # 간선 정보 입력
    arr = list(map(int, input().split()))
    # 연결된 요소의 개수를 구하고 결과 출력
    print(f'#{tc} {union_graph(arr)}')
