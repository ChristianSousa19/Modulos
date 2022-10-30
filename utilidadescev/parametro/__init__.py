def aumentar(preco, aumento, show=False):
    preco = preco + (preco * aumento) / 100
    if show:
        return moeda(preco)
    else:
        return preco
def diminuir(preco, reducao, show=False):
    preco = preco - (preco * reducao) / 100
    if show:
        return moeda(preco)
    else:
        return preco
def dobro(preco, show=False):
    preco *= 2
    if show:
        return moeda(preco)
    else:
        return preco
def metade(preco, show=False):
    preco /= 2
    if show:
        return moeda(preco)
    else:
        return preco
def moeda(preco):
    return f'R${preco:.2f}'.replace('.', ',')
def resumo(valor= 0, porcentagema= 0, porcentagemr=0):
    print('-' * 30)
    print('ANALISANDO PREÇO'.center(30))
    print('-' * 30)
    print(f'Preço analisado:\t{moeda(valor)}')
    print(f'Metado do preço: \t{moeda(metade(valor))}')
    print(f'Dobro do preço: \t{moeda(dobro(valor))}')
    if porcentagema > 9:
        print(f'{porcentagema}% de aumento: \t{moeda(aumentar(valor,porcentagema))}')
    else:
        print(f'{porcentagema}% de aumento: \t\t{moeda(aumentar(valor, porcentagema))}')
    if porcentagemr > 9:
        print (f'{porcentagemr}% de redução: \t{moeda(diminuir(valor,porcentagemr))}')
    else:
        print(f'{porcentagemr}% de redução: \t\t{moeda(diminuir(valor, porcentagemr))}')
    return '-' * 30

