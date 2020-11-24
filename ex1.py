#1) Escreva um programa que recebe como entradas (utilize a função input) dois números
#inteiros correspondentes à largura e à altura de um retângulo, respectivamente. O
#programa deve imprimir uma cadeia de caracteres que representa o retângulo
#informado com caracteres '#' na saída.


larg = int(input("Digite a largura: "))
altu = int(input("Digite a altura: "))
# input de entrada das variaveis altura e largura
linha = 0
coluna = 0

while linha < altu:
    while coluna < larg:
        print("#", end="")
        coluna = coluna + 1
    print()

    linha = linha+1
    coluna = 0