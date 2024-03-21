# 백트래킹

# 중복된 순열
# 1~3까지 숫자 배열이 있을 때
# 111, 112, 113 ,121, 122, 123 ... 332, 333

# 재귀 함수 => 특정 시점으로 돌아오는 게 핵심 
# 파라미터 :  바로 작성 X, 구조를 먼저 잡으면 자연스럽게 필요한 변수들이 보인다.
arr = [i for i in range(1,4)]
path = [0]*3

# 순열
# 123, 132,213,231,312,321
# 숫자는 한번만 사용 

def dfs(level):
    # 기저 조건
    # 이 문제에서는 3개를 뽑았을 때까지 반복
    if level == 3:
        print(path)
        return 
    # 들어가기 전
    # 다음 재귀 호출
    # - 다음에 갈 수 있는 곳들은 어디이낙?
    # 기본 코드
    for i in range(len(arr)):
        path[level]=arr[i]
        dfs(level+1)
    # 갔다와서 할 로직
dfs(0)

def dfs(level):
    # 기저 조건
    # 이 문제에서는 3개를 뽑았을 때까지 반복
    if level == 3:
        print(path)
        return 
    # 들어가기 전
    # 다음 재귀 호출
    # - 다음에 갈 수 있는 곳들은 어디이낙?
    # 기본 코드
    for i in range(len(arr)):
        # 여기는 못가
        # 또는 갈 수 있을 때만, 아래 코드를 실행해라.
        # 갈 수 없는 경우를 활용
        if arr[i] not in path:
            continue

        path[level]=arr[i]
        dfs(level+1)
        # 갔다와서 할 로직
        # 기존 방문을 초기화
        path[level] = 0 

dfs(0)
arr = range(1,11):
temp = []
def sum_set(temp):
    if sum(temp) == 10:
        print(temp)
        return
    for i in range(1,11):
        
    