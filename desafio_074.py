'''Este código vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso,
 mostra a listagem de números gerados e também indique o menor e o maior valor que estão na tupla'''
from random import randint

n = (randint(1, 10), randint(1, 10),randint(1, 10),randint(1, 10),randint(1, 10))
print('Os númeors sorteados foram: ', end='')
for x in n:
    print(f'{x}.. ', end='')
print(f'\nO maior valor sorteado foi {max(n)}')
print(f'O menor valor sorteado foi {min(n)}')