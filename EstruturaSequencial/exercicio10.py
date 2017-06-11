# Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Farenheit.
print('Celsius -> Farenheint 1.0')
print('\n')
while True:
    c = float(input('Digite o valor de Celsius a ser convertido: '))
    print('{} graus Celsius equivalem a {:.1f} graus Farenheit'.format(c, 1.8 * c + 32))
    print('\n')
