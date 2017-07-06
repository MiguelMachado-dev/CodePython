# Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em
# metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de
# 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros,
# que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas
# e o preço total.

area = float(input('Qual o tamanho da área em m² a ser pintada? '))
tintaUsada = area / 3
Latas = tintaUsada / 18
Valor = Latas * 80.00

print('Será(ão) necessário(s) {:.1f} latas de tinta, que darão {:.2f} reais!'.format(Latas, Valor))