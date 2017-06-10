#Faça um Programa que peça a temperatura em graus Farenheit, transforme e mostre a temperatura
#em graus Celsius.
#C = (5 * (F-32) / 9).
print('Farenheit -> Celsius 1.0')
print('\n')
while True:
    f = float(input('Temperatura em Farenheit: '))
    print('A temperatura em Celsius será de: {:.1f}°C'.format((5 * (f - 32) / 9)))
    print('\n')