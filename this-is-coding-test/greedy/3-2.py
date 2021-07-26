n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort(reverse=True)

result = (data[0]*k+data[1])*(m//(k+1)) + data[0]*(m%(k+1))

print(result)