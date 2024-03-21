# person = ['A','B','C','D','E']
# visited = set()
# cnt = 0
# def combi(row,visited,result):
#     global cnt
#     if len(visited) == 3:
#         cnt +=1
#         print(result)
#         return
#
#     for next in range(len(person)):
#         if next not in visited and not result or result[-1] < person[next]:
#             visited.add(next)
#             result.append(person[next])
#             combi(row+1,visited,result)
#             result.pop()
#             visited.remove(next)
#
# combi(0,visited,[])

# 주사위 3개 독립적으로
N =3
path = []
# 중복 순열이기 때문에 i를 넣어줌
def func(lev,start):
    if lev ==N:
        print(path)
        return

    for i in range(start,7):
        path.append(i)
        func(lev+1,i)
        path.pop()
func(0,1)
