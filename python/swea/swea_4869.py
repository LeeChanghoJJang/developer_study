def paper_cut(n):
	if n==1:
		return 1
	elif n==2:
		return 3
	else:
		return paper_cut(n-2)*2 + paper_cut(n-1)
total_count = int(input())
for i in range(1,total_count+1):
	horizental = int(input())
	print('#{} {}'.format(i,paper_cut(horizental//10)))