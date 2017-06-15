# Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que
# calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58

print('Seu peso ideal em apenas um passo!')
print('\n')

while True:
    h = float(input('Digite sua altura: '))
    print('Seu peso ideal é de {:.1f}kg.'.format((72.7 * h)- 58))
    print('\n')
