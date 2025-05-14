import random
def somar(m, n):
    return m + n


def subtrair(m, n):
    return m - n


def multiplicar(m, n):
    return m * n


def dividir(m, n):
    if n!=0:
        return m / n
    else:
        return "Erro: divisão por zero!"


escolha = input('Escolha a operação: (soma, subtração, multiplicação ou divisão): ')
num1 = int(random.randint(1, 100))
num2 = int(random.randint(1, 100))

if escolha == 'soma':
    print('Resultado: ', somar(num1, num2))
elif escolha == 'subtração':
    print('Resuldado: ', subtrair(num1, num2))
elif escolha == 'multiplicação':
    print('Resultado: ', multiplicar(num1, num2))
elif escolha == 'divisão':
    print('Resultado: ', dividir(num1, num2))
else:
    print('Operação inválida')
