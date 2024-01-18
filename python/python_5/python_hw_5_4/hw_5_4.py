# 아래 함수를 수정하시오.
def find_min_max(args):
    min_value= float('inf')
    max_value = 0
    for i in args:
        if i > max_value:
            max_value= i 
        if i < min_value:
            min_value = i
    return min_value,max_value

result = find_min_max([3, 1, 7, 2, 5])
print(result)  # (1, 7)
