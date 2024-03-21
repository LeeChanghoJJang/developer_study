# N= ['A','B','C','D','E']
#
# for i in range(1<<len(N)):
#     for j in range(len(N)):
#         if i&(1<<j):
#             print(N[j],end=' ')
#     print()

arr = ['A','B','C','D','E']
n = len(arr)

def get_count(tar):
    cnt = 0
    for i in range(n):
        # 1비트 1인지 확인
        if tar&0x1:
            cnt +=1
        # right shift 비트 연산자 -> 오른쪽 긑 비트를 하나씩 제거
        tar >>=1
    return cnt

result = 0
for tar in range(1<<n):
    if get_count(tar) >= 2:
        result +=1
print(result)

