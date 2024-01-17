total_count = int(input())
def eraser_equals(alphabet):
	stack=[]
	cnt=0
	for index in range(len(alphabet)):
		if len(stack)==0 or alphabet[index] != stack[-1]:
			stack.append(alphabet[index])
		else:
			stack.pop()
			cnt+=1
	return len(stack)        

for index in range(1,total_count+1):
	alphabet = list(input())
	print('#{} {}'.format(index,eraser_equals(alphabet)))