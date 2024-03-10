import sys
sys.stdin = open('input.txt')
# 첫번째 코드 : 집합 이용 43312KB, 184ms
N = int(input())
employee = set()
for _ in range(N):
    name, work = input().split()
    if work =='enter':
        employee.add(name)
    elif work=='leave':
        employee.remove(name)
employee = sorted(list(employee))
while employee:
    print(employee.pop())
# 두번째 코드 : 딕셔너리 이용 48332KB, 192ms
N = int(input())
temp = dict()
for _ in range(N):
    name,work = input().split()
    if work =='enter':
        temp[name]=work
    else:
        del temp[name]
temp =sorted(temp,reverse=True)
for i in temp:
    print(i)