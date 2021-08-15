def find_rule(num):
	duo_list=[num]
	while True:
		duo_list.append((duo_list[-1] * num) % 10)
		if duo_list[-1] == num: break
	return duo_list
for _ in range(int(input())):
	a,b = map(int, input().split())
	a_list = find_rule(a%10)
	ans = a_list[b%len(a_list)-1]
	if ans==0:ans = 10
	print(ans)