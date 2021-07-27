n = int(input())
fear = list(map(int, input().split()))

fear.sort(reverse=True)
cnt = 0
while True:
	cnt += 1
	if len(fear) <= fear[0]:
		break
	fear = fear[fear[0]:]
	
print(cnt)