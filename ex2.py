#2) Refaça o exercício da questão anterior, imprimindo os retângulos sem preenchimento,
#de forma que os caracteres que não estiverem na borda do retângulo sejam espaços.


largura = int(input("Coloque a largura: "))
print("")
altura = int(input("Coloque a altura: "))
print("")
caractere = "#"

def retângulo(largura, altura, caractere):

    linhacompleta = caractere * largura
    if largura > 2:
        linhavazia = caractere + (" " * (largura - 2)) + caractere
    else:
        linhavazia = linhacompleta

    if altura >= 1:
        print(linhacompleta)
    for i in range(altura - 2):
        print(linhavazia)
    if altura >= 2:
        print(linhacompleta)

retângulo(largura, altura, caractere)