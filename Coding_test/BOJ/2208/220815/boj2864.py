n, m = input().split()

n_1 = ''
n_2 = ''

for i in n:
    if i == '6' or i == '5':
        n_1 += '5'
        n_2 += '6'
    else:
        n_1 += i
        n_2 += i

m_1 = ''
m_2 = ''

for ii in m:
    if ii == '6' or ii == '5':
        m_1 += '5'
        m_2 += '6'
    else:
        m_1 += ii
        m_2 += ii

print(int(n_1) + int(m_1), int(n_2) + int(m_2))