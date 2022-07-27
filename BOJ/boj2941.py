alphas = input()
cro_alphas = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
new_alphas = alphas

for i in cro_alphas:
    if i in new_alphas:
        new_alphas = new_alphas.replace(i, 'A')
print(len(new_alphas))
