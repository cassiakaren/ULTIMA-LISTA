pri_ma = []
seg_ma = []
def cria_matriz(num_linhas, num_colunas):
    for x in range(num_linhas):
        linha = []
        for y in range(num_colunas):
            valor = int(input("Digite o elemento [" + str(x) + "][" + str(y) + "]"))
            linha.append(valor)
        pri_ma.append(linha)
    return pri_ma
def cria_matriz2(num_linhas, num_colunas):
    for x in range(num_linhas):
        linha = []
        for y in range(num_colunas):
            valor = int(input("Digite o elemento [" + str(x) + "][" + str(y) + "]"))
            linha.append(valor)
        seg_ma.append(linha)
    return seg_ma
def dimensoes1(m):
    return len(m)
def dimensoes2(m):
    return len(m[0])
def le_matriz():
    lin = int(input("Digite o número de linhas da primeira matriz: "))
    col = int(input("Digite o número de colunas da segunda matriz: "))
    return cria_matriz(lin, col)
def le_matriz2():
    lin = int(input("Digite o número da primeira matriz: "))
    col = int(input("Digite o número da segunda matriz: "))
    return cria_matriz2(lin, col)

def multiplicarMatriz(pri_ma, seg_ma):
    if dimensoes1(pri_ma) == dimensoes2(seg_ma):
        return True
    else:
        return False


print(le_matriz())
print(le_matriz2())
print(multiplicarMatriz(pri_ma, seg_ma))
