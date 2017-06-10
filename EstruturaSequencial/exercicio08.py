#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
#Calcule e mostre o total do seu salário no referido mês.
print('Cálculo de salário 1.0')
print('\n')
while True:
    ganhohora = float(input('Quanto você ganha por hora? '))
    horatrabalhada = float(input('Quantas horas você trabalha no mês? '))
    s = ganhohora * horatrabalhada
    print('Você ganhará {:.2f} reais no mês em questão.'.format(s))
    print()
