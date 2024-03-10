# 아래 함수를 수정하시오.
def even_elements(my_list):
    even_stack=[]
    while my_list:
        a = my_list.pop(0)
        if a%2==0:
            even_stack.extend([a])
    return even_stack
            
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = even_elements(my_list)
print(result)
