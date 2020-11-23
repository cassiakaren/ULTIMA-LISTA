'''Escreva um programa que recebe como entradas (utilize a função input) dois números
inteiros correspondentes à largura e à altura de um retângulo, respectivamente. O
programa deve imprimir uma cadeia de caracteres que representa o retângulo
informado com caracteres '#' na saída.'''
def func_ret():
    altura=[]
    retangulo=[]
    a=int(input('digite a altura: '))
    b=int(input('digite a largura: '))
    for item in range (a):
        altura+=[item]
    print(altura)
    for iten in range(b):
        retangulo.append(altura)
    print(retangulo)
    for linha in range(len(retangulo)):
        for coluna in range (len(retangulo[0][:])):
            print ('#', end = '')
        print()
        
func_ret()
    