import sys
sys.stdin = open('input.txt')
password = {'0001101':0,'0011001':1,'0010011':2,'0111101':3,'0100011':4,'0110001':5,'0101111':6,'0111011':7,'0110111':8,'0001011':9}
def search(arr):
    i=0
    result =[]
    cnt=0
    while i < len(arr)-7:
        if arr[i:i+7] in password.keys() and arr[i+7*(8-cnt)-1]=='1':
            result.append(password[arr[i:i+7]])
            i+=7
            cnt +=1
        elif cnt==8:
            break
        else:
            i+=1
    return result

def counting(arr):
    temp = 0
    for i in range(len(arr)):
        if i%2 ==0:
            temp += arr[i]*3
        else:
            temp += arr[i]
    if temp % 10 ==0:
        return True
    else:
        return False

T = int(input())
for tc in range(1,T+1):
    obj=0
    N,M = map(int,input().split())
    for _ in range(N):
        arr = input()
        result = search(arr)
        if result and counting(result) and sum(result) > obj:
            obj = sum(result)
    print(f'#{tc} {obj}')
