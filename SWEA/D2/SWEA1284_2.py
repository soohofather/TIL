T = int(input())
for test_case in rage(1 + T):
    P, Q, R, S, W = map(int, input(),split())

    A = W * P

    if R > W:
        B = Q
    else:
        B = Q + S*(W-R)
        
    print(f'#{test_case} {min(A, B)}')