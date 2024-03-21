import sys
sys.stdin = open('input.txt')

for tc in range(1,int(input())+1):
    N,M = map(int,input().split())
    # 컨테이너들 모음 (가장 베스트는 가장 무거운것을 트럭 적재용량에 딱맞게 넣는것)
    # 따라서 무거운 컨테이너부터 각 트럭이 담을 수 있는지 판단(그리디)
    containers = sorted(map(int,input().split()),reverse=True)
    # 수하물 싣을수 있는 양의 트럭 모음(1대에 한 개밖에 못 싣음)
    # 그래서 트럭은 오름차순(용량이 적은것부터)
    truck = sorted(map(int,input().split()))
    result = []
    visited = [0] * (len(truck)+1)
    for i in range(len(containers)):
        for j in range(len(truck)):
            # 각 트럭이 채워지지 않았고, 컨테이너 무게가 트럭 적재용량보다 작을때
            if not visited[j] and containers[i] <= truck[j]:
                # 적재할 수하물 무게를 result에 담음
                result.append(containers[i])
                # 트럭 채웠다는 표시
                visited[j]=1
                # break의 이유는 한 대에 하나만 싣기 위해
                break
        # 트럭이 다 꽉찼거나, 컨테이너를 다 싣었으면 종료
        if len(result) == min(len(containers),len(truck)):
            break
    print(f'#{tc} {sum(result)}')