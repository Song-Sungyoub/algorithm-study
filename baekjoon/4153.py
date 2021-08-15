while True:
	t_length = list(map(int, input().split()))
	if t_length[0] == 0 and t_length[1] == 0 and t_length[2]==0:
		break
	t_length.sort()
	if t_length[2]**2 == t_length[1]**2 + t_length[0]**2:
		print("right")
	else:
		print("wrong")