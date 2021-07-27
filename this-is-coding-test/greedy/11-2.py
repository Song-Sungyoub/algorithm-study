s = list(map(int, list(input())))

result = 1
for i in s:
	if i == 0:
		continue
	result *= i
print(result)
	