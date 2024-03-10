total_count = int(input())
total_set = list(range(1,13))
for index in range(total_count):
    set_cnt,set_sum = map(int,input().split())
    ans=0
    for i in range(1<<len(total_set)):
        now_cnt,now_sum = 0, 0
        for j in range(len(total_set)):
            if i&(1<<j):
                now_sum = total_set[j]
                now_cnt +=1
        if now_sum == set_sum and now_cnt ==set_cnt:
            ans +=1
    print(f'{index+1} {ans}')