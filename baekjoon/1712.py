a,b,c = map(int, input().split())

result = a/(c-b) + 1

if c-b>0:
	print(result)
else:
	print(-1)
