# 아래 함수를 수정하시오.
def add_item_to_dict(args1,key,value):
    new_dict = {key:value}
    args1.update(new_dict)
    return args1


my_dict = {'name': 'Alice', 'age': 25}
result = add_item_to_dict(my_dict, 'country', 'USA')
print(result)