# Tendo como dados de entrada a altura e o sexo de uma pessoa, construa um algoritmo
# que calcule seu peso ideal, utilizando as seguintes fórmulas:
# Para homens: (72.7*h) - 58
# Para mulheres: (62.1*h) - 44.7 (h = altura)
# Peça o peso da pessoa e informe se ela está dentro, acima ou abaixo do peso.

print('Seu peso ideal completo!')
print('\n')

s = input('Insira seu sexo [f/m]: ').lower()
h = float(input('Insira sua altura: '))
pcm = (72.7*h) - 58
pcf = (62.1*h) - 44.7
if s == 'f':
    print('Seu peso ideal seria {:.1f}kg.'.format(pcf))
if s == 'm':
    print('Seu peso ideal seria {:.1f}kg.'.format(pcm))

p = float(input('Insira seu peso real: '))
if s == 'f' and p < pcf:
    print('Você está abaixo do peso!')
elif s == 'm' and p < pcm:
    print('Você está abaixo do peso!')
else:
    print('Você está acima do peso!')
