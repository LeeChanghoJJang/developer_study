T = int(input())
N= 0
arr =[]
def get_result():
    a=0
    b = (len(arr)+1)//2

    for turn in range(len(arr)):
        if turn % 2 ==0:
            print(arr[a],end=' ')
            a+=1
        else:
            print(arr[b],end=' ')
            b+=1

for tc in range(1,T+1):
    N = int(input())
    arr = list(map(str,input().split()))
    print(f'#{tc}' ,end = '')
    get_result()
    print()