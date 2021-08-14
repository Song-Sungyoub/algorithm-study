def find_keys(dict, val):
	a = list(key for key, value in dict.items() if value == val)
	if len(a) > 1:
		return a[1]
	return a[0]

n = int(input())
arr = sorted([int(input()) for _ in range(n)])

d_arr = {}
for i in set(arr):
	d_arr[i]=0
for i in arr:
	d_arr[i]+=1

print(f'{sum(arr)/n:.0f}')
print(arr[n//2])
print(find_keys(d_arr, max(d_arr.values())))
print(arr[-1]-arr[0])