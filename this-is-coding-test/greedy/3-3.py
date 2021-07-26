n, m = map(int, input().split())
data = []
for _ in range(n):
	data.append(list(map(int, input().split())))
	
print(max([min(i) for i in data]))