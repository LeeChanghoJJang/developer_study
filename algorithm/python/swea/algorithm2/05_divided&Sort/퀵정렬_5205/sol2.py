import sys
sys.stdin = open('input.txt')

def quick(arr):
    if len(arr) <=1:
        return arr
    pivot = arr[len(arr)//2]
    less, equal, greater =[],[],[]
    for num in arr:
        if num <pivot:
            less.append(num)
        elif num == pivot:
            equal.append(num)
        elif num > pivot:
            greater.append(num)
    return quick(less) + quick(equal) + quick(greater)