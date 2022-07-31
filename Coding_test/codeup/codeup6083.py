r, g, b = map(int, input().split())
cnt = 0

for i in range(r):
  for ii in range(g):
    for iii in range(b):
      cnt += 1
      print(i, ii, iii)
print(cnt)
      