 import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1,T+1):
    # 총 N개의 수가 나열됨
    # 연속된 1이 딱 K개 만큼 있어야 함
    N,K = map(int,input().split())
    puzzle = [list(map(int,input().split())) for _ in range(N)]
    # 최종적으로 퍼즐에 들어갈 수 있는 낱말갯수를 complete으로 설정
    complete = 0
    # 가로 검사 : 열 우선순회 방식으로 검사
    for row in range(N):
        # 1이 연속적으로 있는 개수를 세기 위한 변수 cnt 설정
        cnt=0
        for col in range(N):
            # 이전까지의 cnt가 K이고, 해당 위치값이 0이면 complete추가 후 cnt 갱신
            if cnt == K and puzzle[row][col]==0:
                complete += 1
                cnt=0
            # 이전까지의 cnt가 K-1이고, 해당 위치값이 1이면 complete추가 후 cnt 갱신
            elif cnt == K-1 and puzzle[row][col] == 1 and col==N-1:
                complete += 1
                cnt=0
            # 위에 저촉되지 않는 한 위치값이 1이면 cnt 추가
            elif puzzle[row][col]:
                cnt += 1
            # 위에 저촉되지 않는 한 위치값이 0이면 cnt = 0 초기화
            elif puzzle[row][col] == 0:
                cnt = 0
    # 세로 검사
    for col in range(N):
        cnt = 0
        for row in range(N):
            # 이전까지의 cnt가 K이고, 해당 위치값이 0이면 complete추가 후 cnt 갱신
            if cnt == K and puzzle[row][col] == 0:
                complete += 1
                cnt = 0
            # 이전까지의 cnt가 K-1이고, 해당 위치값이 1이면 complete추가 후 cnt 갱신
            elif cnt == K - 1 and puzzle[row][col] == 1 and row==N-1:
                complete += 1
                cnt = 0
            # 위에 저촉되지 않는 한 위치값이 1이면 cnt 추가
            elif puzzle[row][col]:
                cnt += 1
            # 위에 저촉되지 않는 한 위치값이 0이면 cnt = 0 초기화
            elif puzzle[row][col]==0:
                cnt = 0
    print(f'#{tc} {complete}')

# 강사님 풀이(1번째)
T = int(input())
for tc in range(1,T+1):
    N, K = map(int,input().split())
    arr = [list(map(int,input().split())) +[0] for _ in range(N)] + [[0] + (N+1)]
    # 가로 세로로 0으로 둘러싸인 행과 열 추가됨
    N+=1
    ans = 0
    for i in range(N):
        cnt = 0
        for j in range(N):
            if arr[i][j]:
                cnt+=1
            else:
                if cnt==K:
                    ans+=1
                cnt=0

    for j in range(N):
        cnt = 0
        for i in range(N):
            if arr[i][j]:
                cnt+=1
            else:
                if cnt==K:
                    ans+=1
                cnt=0
    print(f'#{tc} {ans}')
# 강사님 풀이(2번째)
T = int(input())
for tc in range(1,T+1):
    N,K = map(int,input().split())
    m = [list(map(int,input().split())) for i in range(N)]
    cnt = 0
    for i in range(N):
        r=0
        c=0
        for j in range(N):
            if m[i][j]:
                c+=1
            else:
                if c==K:
                    cnt+=1
                c=0
            if m[j][i]:
                r+=1
            else:
                if r==K:
                    cnt+=1
                r=0
        if c==K:
            cnt +=1
            c=0
        if r==K:
            cnt+=1
            r=0
        print(f'#{tc} {cnt}')


