import sys

sys.stdin = open('input.txt')


# 순열을 계산하는 함수
def permutations(idx, result):
    global min_val

    # 현재 결과가 최소값보다 크거나 같으면 중단
    if result >= min_val:
        return

    # 현재 결과가 목표값 이상이면 최소값 갱신 후 중단
    if result >= B:
        min_val = result
        return

    # 모든 원소를 사용한 경우 중단
    if idx == N:
        return

    # 현재 원소를 포함하는 경우와 포함하지 않는 경우로 재귀 호출
    permutations(idx + 1, result + heights[idx])  # 현재 원소를 포함하는 경우
    permutations(idx + 1, result)  # 현재 원소를 포함하지 않는 경우


# 입력 처리
for tc in range(1, int(input()) + 1):
    N, B = map(int, input().split())  # N: 블록의 수, B: 목표 높이
    heights = list(map(int, input().split()))  # 각 블록의 높이
    min_val = float('inf')  # 최소값 초기화
    permutations(0, 0)  # 순열 함수 호출
    print(f'#{tc} {min_val - B}')  # 결과 출력
