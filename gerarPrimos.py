import sys


def verificaPrimo(num):
    cont = 0
    for i in range(1, num + 1):
        if num % i == 0:
            cont += 1
    if cont != 2:
        return False
    else:
        return True


class gerarPrimos():

    def __init__(self, lim):
        if lim <= 0 or type(lim) != int:
            sys.exit()
        else:
            self.lim = lim

    def gerarPrimos(self):
        lis = []
        for i in range(0, self.lim+1):
            if i == 0 or i == 1:
                lis.append(False)
            elif verificaPrimo(i):
                lis.append(True)
            else:
                lis.append(False)
        self.lista = lis
        return lis

    def imprimirLista(self):
        ls = []
        for i in range(0, len(self.lista)):
            if self.lista[i] == True:
                ls.append(i)

        print(ls)


def lerNum():
    while True:
        num = int(input('Digite um número inteiro maior que 0\n'))
        if num > 0 or type(num) == int:
            break
    return num


def main():
    print('\nEste programa irá gerar uma lista de números primos dentro do intervalo de 0 até o número digitado\n')
    num = lerNum()
    primos = gerarPrimos(num)
    lis = primos.gerarPrimos()
    print(lis)
    primos.imprimirLista()


if __name__ == "__main__":
    main()
