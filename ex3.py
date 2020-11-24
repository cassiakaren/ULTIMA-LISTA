elementos = int(input('digite quantos elementos deseja: '))
l = []
y = 0
while y != elementos:
    append = float(input('digite um numero inteiro:  '))
    l.append(append)
    y += 1
def segmento_maximo(X):
    mf = ma = l[0]
    for x in l[1:]:
        mf = max(x, mf + x)
        ma = max(ma, mf)
    return ma
print('O valor do segmento maximo é igual a: ', segmento_maximo(l))