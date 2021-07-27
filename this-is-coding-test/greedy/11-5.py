n, m = map(int, input().split())
balls = list(map(int, input().split()))

cnt = 0
for i in range(len(balls)):
	for j in balls[i+1:]:
		if balls[i]!=j:
			print(balls[i],',',j)
			cnt+=1			
print(cnt)