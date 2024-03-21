import sys
sys.stdin = open('input.txt')
for tc in range(1,11):
    # 테스트케이스 번호랑 목적지 route의 개수 파악
    N, route_cnt = map(int,input().split())
    # 간선의 목록을 리스트로 저장
    order = list(map(int,input().split()))
    # 출발지를 따로 모아서 front로 저장
    front = order[::2]
    # 도착점을 따로 모아서 end로 저장
    end = order[1::2]
    # 출발점과 도착점을 연결하는 routes 리스트 작성
    routes = list(zip(front,end))
    # 출발점과 도착점을 연결하기 위해 graph 2차원 배열에
    # 출발점을 행으로, 도착점을 열로 하여 값을 1로 저장
    graph = [[0] * 100 for _ in range(100)]
    for i,j in routes:
        graph[i][j] = 1
    cnt=0
    # 큐 대신 리스트로 BFS 과정 수행
    queue = [0]
    while queue:
        # start는 항상 0에서 시작함
        start = queue.pop()
        # 연결정보가 저장된 graph를 순회하여 연결된 도착점 조회
        # 연결되었으면 다음에 순회하기 위해 queue에 저장
        for y in range(100):
            if graph[start][y]:
                queue.append(y)
        # 도착점 발견 시, cnt 1추가하여 반환
        if 99 in queue:
            cnt=1
            break
    print(f'#{tc} {cnt}')