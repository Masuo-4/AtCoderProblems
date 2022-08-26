year = int(input())
if year % 4 == 2:
	print(year)
elif year % 4 == 0:
	print(year + 2)
else:
	print(year + year % 4)
