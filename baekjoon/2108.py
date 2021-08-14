n = int(input())
arr = [int(input()) for _ in range(n)]

s_arr = list(set(arr))
d_arr = {}
for i in s_arr:
	d_arr[i]=0
for i in arr:
	d_arr[i]+=1
print(f'{sum(arr)/n:.1f}')
print(arr[n//2])
print(max(d_arr))
print(max(arr)-min(arr))