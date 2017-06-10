#Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.
print('Calcular área de quadrado e seu dobro -1.0-')
print('\n')
while True:
    l = float(input('Qual o lado do quadrado? '))
    print('A área do quadrado é de {} e seu dobro de área é {}.'.format(l * l, (l * l) * 2))
    print()
    