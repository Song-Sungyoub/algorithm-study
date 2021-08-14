def find_rule(num):
	tmp = num
	duo_list=[]
	while True:
		duo_list.append(tmp)
		tmp = (tmp * num) % 10
		if tmp == num:
			break
	return duo_list
answer = []
n = int(input())
for _ in range(n):
	a,b = map(int, input().split())
	a_list = find_rule(a%10)
	ans = a_list[b%len(a_list)-1]
	if ans==0:
		ans = 10
	answer.append(ans)
print('\n'.join(map(str, answer)))

# 강대원 수병님이 아이스크림 사준 문제