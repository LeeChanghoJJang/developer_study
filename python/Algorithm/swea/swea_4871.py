def dfs(start,end):
	stack =[] # 스택 초기화
	visited=[False]*(total_node+1) # 방문 여부를 검사할 행렬
	stack.append(start) # 시작점 스택 삽입
	while stack:
        # 지금 현재 스택을 꺼내어 현재 값에 할당
		now = stack.pop()
        # 현재 들렀다는 것을 표시
		visited[now] = True
        # 1부터 total_node 까지 다 들러봄
		for next in range(total_node+1):
            #방문하지 않았으며 연결되어 있다면 
			if not visited[next] and node[now][next]:
				stack.append(next)
	if visited[end]:
		return 1 # 들렀다는 것 표시
	else:
		return 0

total_count = int(input())
for tc in range(total_count):
	total_node, total_line = map(int,input().split())
	node = [[0 for _ in range(total_node+1)] for _ in range(total_node+1)]
    # 연결선 total_line만큼 반복해어 연결되있는지 파악
	for _ in range(total_line):
    	#인접행렬 정보 입력
		front,end = map(int,input().split())
		node[front][end] =1
    # 검사를 위한 첫시작과 끝점 
	start,finish = map(int,input().split())
	print(f'#{tc+1} {dfs(start,finish)}')