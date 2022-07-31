a, b = input().split()

c = bool(int(a))
d = bool(int(b))


print((c and d) or ((not c) and (not d)))