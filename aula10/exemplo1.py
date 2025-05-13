import random
import os

n = random.randint(1, 5)
m = random.randint(1, 5)

print(n, m)

os.system('cls')
list_numeros = [random.randint(1, 10) for i in range(5)]
print(list_numeros)


def gerar_numeros(i, f, q):
    lst_num = [random.randint(i, f) for num in range(q)]
    return lst_num


ini = int(input('informe o primeiro número: '))
fin = int(input('Informe o último número: '))
qtd = int(input('Quantos números? '))

numeros = gerar_numeros(ini, fin, qtd)
print(numeros)
