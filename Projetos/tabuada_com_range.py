print('{:=^30}'.format('Tabuada'))

while True:
    x = int(input('A tabuada de qual número deseja saber? '))
    y = int(input('Ate qual número deseja saber a tabuada do número inserido previamente? '))
    for i in range(y):
        print('{} x {} = {}'.format(i, x, i * x))
# Tabuada feita com range.
# Usuário escolhe o número que quer saber a tabuada e quantas vezes multiplica-lo.
# Exemplo;
# Saber tabuada do número 5
# Até o número 5, então ele digitaria 6.
# Assim, ficaria;
# 5 x 0 = 0
# 5 x 1 = 5
# 5 x 2 = 1 0
# 5 x 3 = 15
# 5 x 4 = 20
# 5 x 5 = 25
