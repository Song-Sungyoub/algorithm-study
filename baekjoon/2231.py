n = int(input())

s = 0
for i in range(1, n+1):
	if i + sum(list(map(int, list(str(i))))) == n:
		s = i
		break

print(s)
