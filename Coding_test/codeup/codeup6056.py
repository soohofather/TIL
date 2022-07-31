a, b = input().split()

c = bool(int(a))
d = bool(int(b))


print((c and (not d)) or ((not c) and d))