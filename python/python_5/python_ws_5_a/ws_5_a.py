N = 9
data_1 = '123456789'
arr_1 = []
# 아래에 코드를 작성하시오.
for alpha in data_1:
    arr_1.append(alpha)
print(arr_1)

M = 15
data_2 = '1 2 3 4 5 6 7 8 9 10 11 12 13 14 15'
# 아래에 코드를 작성하시오.
for digit in data_2.split():
    if int(digit)%2:
        print(int(digit))
