T = int(input())

for i in range(T):
  n = input()
  A = 0

  if n == n[::-1]:
    A += 1
  else:
    A = 0

  print(f'#{i+1}', A)
