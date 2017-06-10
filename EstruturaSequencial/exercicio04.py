#Faça um Programa que peça as 4 notas bimestrais e mostre a média.
print('Calcular Média 1.0')
n1 = float(input('Insira a nota da primeira prova: '))
n2 = float(input('Insira a nota da segunda prova: '))
n3 = float(input('Insira a nota da terceira prova: '))
n4 = float(input('Insira a nota da quarta prova: '))

print('A media das notas {}, {}, {} e {} é igual a {}'.format(n1, n2, n3, n4, (n1 + n2 + n3 + n4) / 4))