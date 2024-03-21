'''
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
'''
def dfs(i):
    visited =[0] * (V+1)
    st = []
    visited[i] = 1
    print(i)
    while True:
        for w in adjl[i]:
            if visited[w]==0:
                st.append(i)   # push(i), i를 지나서
                i = w          # w에 방문
                visited[w] = 1 # 방문해서 할 일
                print(i)
                break
        else:                  # i에 남은 인접 정점이 없으면
            if st: # 스택이 비어있지 않으면
                i = st.pop()
            else: # 스택이 비어있으면(출발점에서 남은정점이 없으면)
                break

def dfs2(i):
    visited[i] = 1
    print(i)
    for w in adjl[i]:
        if visited[w]==0:
            dfs2(w)
V,E = map(int,input().split())
arr =list(map(int,input().split()))
visited =[0] * (V+1)
# 인접리스트
adjl = [[] for _ in range(V+1)] # adjl[i] 행에 i에 인접인 정점번호 저장
for i in range(E):
    n1,n2 = arr[i*2],arr[i*2+1]
    adjl[n1].append(n2)
    adjl[n2].append(n1)

dfs(1)