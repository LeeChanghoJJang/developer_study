T = int(input())
for total_count in range(T):
    N,M = map(int,input().split())
    arr = [input() for _ in range(N)]

def rev_str(total_count):
    for i in range(N):
        # M길이 회문 추적
        for j in range(N-M+1):
            # row 방향
            if arr[i][j:j+M] == arr[i][j:j+M][::-1]:
                print(f'#{total_count} {arr[i][j:j+M]}')
                return # 종료 위함
            # col 방향
            for k in range(M//2):
                if arr[j+k][i] != arr[j+M-k-1][i]:
                    break
            else: # 회문일 때 동작
                print(f'#{total_count}',end='')
                for l in range(M):
                    print(arr[j+l][i],end='')
                print()
                return #종료
rev_str(total_count+1)