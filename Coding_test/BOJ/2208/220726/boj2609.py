a, b = map(int, input().split())

def gcd(a, b):
    o = []
    p = []
    q = []
    for i in range(1, a + 1):
        if a % i == 0:
            o.append(i)
    for ii in range(1, b + 1):
        if b % ii == 0:
            p.append(ii)
    for iii in o:
        if iii in p:
            q.append(iii)
    return max(q)
def lcm(a, b):
    r = []
    s = []
    t = []
    for iii in range(1, b + 1):
        r.append(iii * a)
    for iiii in range(1, a + 1):
        s.append(iiii* b)
    for iiiii in r:
        if iiiii in s:
            t.append(iiiii)
    return min(t)

print(gcd(a, b))
print(lcm(a, b))