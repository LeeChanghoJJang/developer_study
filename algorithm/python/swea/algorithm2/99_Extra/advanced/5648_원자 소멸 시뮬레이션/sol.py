import sys
sys.stdin = open('input.txt')
# 상하좌우 방향
ways = {0:(0,1),1:(0,-1),2:(-1,0),3:(1,0)}
for tc in range(1,int(input())+1):
    N = int(input())
    # 원자들의 정보를 모두 모을 곳
    wonja = []
    for _ in range(N):
        x, y, way, energy = map(int,input().split())
        # 범위를 2배로 할것임
        x = 2 * x
        y = 2 * y
        f_time = 0
        wonja.append([x,y,way,energy,f_time])
    result = 0
    # 원자들의 순서, 에너지량, 시간, 터져서 사라져야할 여부(팡) 저장
    info={}

    for _ in range(4004):
        # 전부 탐색했을 때 check가 변하지 않으면 종료할 것
        check = 0
        for i in range(N):
            x, y, way, energy, time = wonja[i]
            # 에너지양이 전부 다 result값에 더해서 없어지거나, 소멸된 경우
            time +=1
            check += (energy > 0)
            pang = 0
            if energy == 0:
                continue
            nx = x + ways[way][0]
            ny = y + ways[way][1]
            wonja[i][0], wonja[i][1], wonja[i][4] = nx, ny, time
            if not (abs(nx)<=2000 and abs(ny)<=2000):
                wonja[i][3] = 0
            if (nx,ny) not in info.keys():
                info[(nx,ny)] = [i, energy, time, 0]
            else:
                # 기존에 [(nx,ny)]에 원자가 있으면 그 정보 호출
                existing_num, existing_energy, existing_time, pang = info[(nx,ny)]
                # 같은 시간에 같은 위치에 있다면
                if time == existing_time:
                    # 두 원자의 정보를 같이 저장하며, 시간은 같으므로 time저장
                    # 그리고 팡여부를 저장
                    info[(nx,ny)] = [i, wonja[i][3] + existing_energy, time, 1]
                    # 이제 두 원자는 볼일 없으므로 energy=0 처리해서 앞에서 넘어가게끔
                    wonja[i][3] = 0
                    wonja[existing_num][3] = 0
            # 원자의 위치가 x,y에서 nx,ny로 넘어갔으므로 기존 x,y값은 지우기
            # 미포함된 부분은 이동하기 전에 지우는 거면, 글로 이동을 먼저 한 경우에는?
            if info.get((x, y)):
                del info[(x, y)]

        for i in info.copy().keys():
            if info[i][-1]:
                result += info[i][1]
                del info[i]
        if check == 0:
            for i in info.keys():
                if abs(i[0]) <= 2000 and abs(i[1]) <= 2000:
                    result += info[i][1]
            break

    print(f'#{tc} {result}')

