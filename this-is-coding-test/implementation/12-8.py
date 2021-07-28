s = list(input())

s.sort()

sum = 0
new = []
for i in s:
	if '0'<=i<='9':
		sum += int(i)
	else:
		new.append(i)
print(''.join(new)+str(sum))