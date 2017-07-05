# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas
# no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são
# descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um
# programa que nos dê:
# a) salário bruto.
# b) quanto pagou ao INSS.
# c) quanto pagou ao sindicato.
# d) o salário líquido.
# calcule os descontos e o salário líquido, conforme a tabela abaixo:
# + Salário Bruto : R$
# - IR (11%) : R$
# - INSS (8%) : R$
# - Sindicato ( 5%) : R$
# = Salário Liquido : R$
# Obs.: Salário Bruto - Descontos = Salário Líquido.

ganhoHora = float(input('Quanto você ganha por hora: R$'))
horaTrabalhada = int(input('Quantas horas você trabalha no mês: '))

salarioBruto = ganhoHora * horaTrabalhada
IR = salarioBruto * 0.11
INSS = salarioBruto * 0.08
sindicato = salarioBruto * 0.05

print('Salário Bruto: R${:.2f}'.format(salarioBruto))
print('Imposto de Renda: R${:.2f}'.format(IR))
print('INSS: R${:.2f}'.format(INSS))
print('Sindicato: R${:.2f}'.format(sindicato))
print('Salário Liquido: R${:.2f}'.format(salarioBruto - IR - INSS - sindicato))