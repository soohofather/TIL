T = int(input())

for i in range(T):
  a, b, c, d = map(int, input().split())

  e = a + c
  f = b + d

  A = 0
  B = 0

  if f < 59:
    A = e
    B = f
  else:
    A = e + 1
    B = f - 60

  print(f'#{i+1}', A - 12 if A > 12 else A , B)