n,m = map(int, input().split())
l = list(map(int, input().split()))

jack = -1
ll = len(l)

for i in range(0,ll-2):
	for j in range(i+1,ll-1):
		for k in range(j+1,ll):
			tmp = l[i] + l[j] + l[k]
			if jack <= tmp <=m:
				jack = tmp

print(jack)