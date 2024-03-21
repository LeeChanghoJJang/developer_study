import sys

# 입력 파일을 표준 입력으로 변경
sys.stdin = open('input.txt')

# 메인 함수
for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())  # 출발점(N)과 도착점(M) 입력
    temp = {N}  # 현재 위치를 나타내는 집합 초기화
    result = 0  # 결과값 초기화
    visited = [0] * (int(1e6) + 1)  # 방문 여부를 저장할 리스트 초기화

    # 출발점이 도착점보다 큰 경우, 10초 단위로 이동하여 도착점에 도달할 수 있는 최소 이동 횟수 계산
    if N > M:
        result = (N - M) // 10  # 10초 단위로 이동하여 도착점에 도달하는데 필요한 횟수 계산
        temp = {N - (N - M) // 10 * 10}  # 도착점에 도달하기 직전 위치를 저장

    time = -1  # 시간 초기화
    visited[N] = 1  # 출발점 방문 표시

    # BFS를 이용하여 최소 이동 횟수 계산
    while time <= int(1e6):  # 최대 100만번까지 반복
        time += 1  # 시간 증가
        next_temp = set()  # 다음 이동 위치를 저장할 집합 초기화
        for i in temp:
            if i == M:  # 도착점에 도착한 경우
                result += time  # 결과값에 시간 추가
                break
            for next_num in [i - 1, i + 1, i * 2, i - 10]:  # 가능한 다음 이동 위치 계산
                if 0 < next_num <= 1000000 and not visited[next_num]:  # 범위 내에 있고 방문하지 않았을 경우
                    next_temp.add(next_num)  # 다음 이동 위치에 추가
                    visited[next_num] = 1  # 방문 표시
        else:
            temp = next_temp  # 다음 이동 위치를 현재 위치로 업데이트
            continue
        break

    # 결과 출력
    print(f'#{tc} {result}')
