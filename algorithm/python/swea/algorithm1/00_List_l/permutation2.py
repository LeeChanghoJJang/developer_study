### {1,2,3,4,5,6,7,8,9,10} 의 부분집합 구하기

'''
K = 탐색 대상이 된 원소 번호
result = 최종 결괏값 
cnt = 부분집합의 합이 몇이냐 
'''

def powerset(K,result,cnt):
    global count
    count +=1 
    # 배열 arr에 양의 정수만 지속적으로 누적해 나갈것이다.
    # if cnt >10: # 한번이라도 누적합이 10을 넘어섰다면, 앞으로 조사하는 의미가 없다.
    #     return # 더 조사하지 말고 돌아가 
    # 언제까지 조사할 것이냐
    # K번째 원소를 사용한 경우, 사용하지 않은 경우
    if K==N: # 모든 원소에 대해 조사를 마쳤다면
        if cnt ==10 : # 다음 조건 : 부분집합의 합이 10인 경우만
            print(result)
        return # 조사종료
    else: # 아직 조사해야 하는 원소가 남아있는 경우
        # K번째 원소를 사용한 경우
        powerset(K+1,result+[arr[K]],cnt+arr[K])
        # K번째 원소를 사용하지 않은 경우
        powerset(K+1,result,cnt)


N = 10 # 원소의 개수가 N개
arr = list(range(1,11)) # 1부터 10까지
count = 0
powerset(0,[],0)
print(count)