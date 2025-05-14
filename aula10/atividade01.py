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


def calculadora():
    print('Calculadora')
    print('operações: 1 - soma, 2 - subtração, 3 - multiplicação, 4 - divisão')
    escolha = input('Escolha a operação: ')
    num1 = int(random.randint(1, 100))
    num2 = int(random.randint(1, 100))

    print(num1, num2)
    match escolha:
        case '1':
            print('Resultado:', somar(num1, num2))
        case '2':
            print('Resultado:', subtrair(num1, num2))
        case '3':
            print('Resultado:', multiplicar(num1, num2))
        case '4':
            print('Resultado:', dividir(num1, num2))


calculadora()
