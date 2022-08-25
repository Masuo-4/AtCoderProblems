x,y,n = map(int, input().split())
if x <= (y / 3):
	print(x * n)
else:
	print(y * (n // 3) + x * (n % 3))
