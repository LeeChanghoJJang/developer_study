# 2751번 수정렬하기2
# 내코드 (1432ms)
import sys
N= int(sys.stdin.readline())
temp=[]
for i in range(N):
    temp.append(int(sys.stdin.readline()))
for i in sorted(temp):
    print(i)

# 합병정렬(nlogn) (7532ms)
import sys
n=int(sys.stdin.readline())
li=[]

for i in range(n):
    li.append(int(sys.stdin.readline()))

def sort(arr):
    if len(arr)<2:
        return arr
    
    mid=len(arr)//2
    left=sort(arr[:mid])
    right=sort(arr[mid:])

    return merge(left,right)
    
def merge(left,right):
    new_list=[]
    i=0
    j=0
    
    while (i<len(left)) & (j<len(right)):
        if left[i]>right[j]:
            new_list.append(right[j])
            j+=1
        else:
            new_list.append(left[i])
            i+=1
    while (j<len(right)):
            new_list.append(right[j])
            j+=1
    while (i<len(left)):
            new_list.append(left[i])
            i+=1
    return new_list
    
for i in sort(li):
    print(i)