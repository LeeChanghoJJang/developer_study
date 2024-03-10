import sys
sys.stdin = open('input.txt')
import pprint
# 1차 방법 : 메모리 초과
# def find_obj(objective):
#     for i in range(2**N):
#         for j in range(2**N):
#             if int(arr[i][j])==objective:
#                 return arr[i-y][j+x]
#
# def four_divide(cnt,num,row,col,ranges):
#     if cnt < 0:
#         return
#
#     for i in range(row,row + ranges):
#         for j in range(col,col + ranges):
#             arr[i][j] += num
#
#     four_divide(cnt - 1,'1', row, col + ranges//2, ranges//2)
#     four_divide(cnt - 1, '2', row, col, ranges//2)
#     four_divide(cnt - 1, '3', row + ranges//2, col, ranges//2)
#     four_divide(cnt - 1, '4', row + ranges//2, col + ranges//2, ranges//2)
#
# N, objective = map(int,input().split())
# x,y = map(int,input().split())
# arr= [[''] * 2**N for _ in range(2**N)]
# four_divide(N,'',0,0,2**N)
# pprint.pprint(arr)
# print(find_obj(objective))

# 2차 방법 : 수학으로 풀겠다
N, objective = map(int,input().split())
x,y = map(int,input().split())
def find_number(x,y,N):
    result = ''
    while N:
        if x >= 2 ** (N - 1) and y >= 2 ** (N - 1):
            result += '4'
            x -= 2 ** (N - 1)
            y -= 2 ** (N - 1)
        elif x >= 2 ** (N - 1) and y < 2 ** (N-1):
            result += '3'
            x -= 2 ** (N - 1)
        elif x < 2 ** (N - 1) and y < 2 ** (N-1):
            result += '2'
        elif x < 2 ** (N - 1) and y >= 2 ** (N-1):
            result += '1'
            y -= 2 ** (N - 1)
        if x<0 or y<0:
            return -1
        N-=1
    return result

def divided(objective,x,y,depth):
    while objective:
        k, v = divmod(objective,10)
        if v == 1:
            y += 2 ** (depth - 1)
        elif v== 2:
            pass
        elif v==3:
            x += 2 ** (depth - 1)
        elif v==4:
            x += 2 ** (depth - 1)
            y += 2 ** (depth - 1)
        depth+=1
        objective=k
    return [x,y]
location_x,location_y = divided(objective,0,0,1)
x_adj = location_x - y
y_adj = location_y + x
if x_adj < 0 or x_adj >= 2**N or  y_adj < 0 or y_adj >= 2**N:
    print(-1)
else:
    print(find_number(x_adj,y_adj,N))
