# Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
# I) o produto do dobro do primeiro com metade do segundo .
# II) a soma do triplo do primeiro com o terceiro.
# III) o terceiro elevado ao cubo.

while True:
    x = int(input('Insira um número inteiro: '))
    y = int(input('Insira outro número inteiro: '))
    z = float(input('Insira um número real: '))
    print('Operação I = {}'.format((2 * x)+(0.5 * y)))
    print('Operação II = {}'.format((3 * x)+ z))
    print('Operação III = {}'.format(z ** 3))
    print('\n')
