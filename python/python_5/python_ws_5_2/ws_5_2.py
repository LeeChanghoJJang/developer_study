# 아래 함수를 수정하시오.
# def remove_duplicates(new_lst):
#     return list(set(new_lst))
def remove_duplicates(new_lst):
    temp_list =[]
    for i in new_lst:
        if i not in temp_list:
            temp_list.append(i)
    return temp_list


result = remove_duplicates([1, 2, 2, 3, 4, 4, 5])
print(result)
