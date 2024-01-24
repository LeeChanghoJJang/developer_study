# 1004번 어린왕자 (내 풀이)
import sys
N = int(sys.stdin.readline()) # 총 횟수
for i in range(N): # 출발점을 x1,y1, 도착점을 x2,y2로 지정
    x1,y1,x2,y2 = map(int,sys.stdin.readline().split())
    planet_cnt = int(sys.stdin.readline())
    enter = 0
    for i in range(planet_cnt): 
        cx,cy,r = map(int,sys.stdin.readline().split()) # 행성계 좌표 및 반지름 입력
        distance1 = (cx-x1)**2 + (cy-y1)**2 # 출발점에서 행성계까지 거리
        distance2 = (cx-x2)**2 + (cy-y2)**2 # 도착점에서 행성계까지 거리
        if (distance1 < r**2) + (distance2 < r**2)==2: 
            pass # 행성계가 출발점과 도착점 모두 포함하는 경우 --> 경계를 터치할 일 없음
        elif (distance1 < r**2) + (distance2 < r**2)==1:
            enter+=1 # 행성계가 출발점과 도착점 둘 중 하나를 포함하는 경우 --> 반드시 경계 터치
        elif (distance1 < r**2) + (distance2 < r**2)==0:
            pass # 행성계가 출발점과 도착점 둘 다 포함하지 않는 경우 --> 우회해서 갈 수 있음
    print(enter)

# 1004번 어린왕자 (코드개선)
import sys
N = int(sys.stdin.readline()) # 총 횟수
for i in range(N): # 출발점을 x1,y1, 도착점을 x2,y2로 지정
    x1,y1,x2,y2 = map(int,sys.stdin.readline().split())
    planet_cnt = int(sys.stdin.readline())
    enter = 0
    for i in range(planet_cnt): 
        cx,cy,r = map(int,sys.stdin.readline().split()) # 행성계 좌표 및 반지름 입력
        distance1 = (cx-x1)**2 + (cy-y1)**2 # 출발점에서 행성계까지 거리
        distance2 = (cx-x2)**2 + (cy-y2)**2 # 도착점에서 행성계까지 거리
        if (distance1 < r**2) + (distance2 < r**2)==1:
            enter+=1 # 행성계가 출발점과 도착점 둘 중 하나를 포함하는 경우 --> 반드시 경계 터치
    print(enter)
'''코드 리뷰
전체적으로 가독성은 좋지만, 반복되는 경우가 많아 코드가 길어 필요없는 문장 삭제 필요
다른 풀이들과 비교해도 시간이 긴 편은 아니었음(48ms)
'''