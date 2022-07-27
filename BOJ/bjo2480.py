a, b, c = map(int, input().split())

if a == b and b == c:
	print(10000 + (a * 1000) )
elif a != b and b != c and a != c:
	print( ((a if a > b else b) if (a if a > b else b) > c else c) * 100)
else:
	print(1000 + (a if a == b else c) * 100)


