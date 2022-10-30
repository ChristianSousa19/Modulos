from utilidadescev import parametro

num=float(input("Digite o preço R$: "))
print(f"O dobro de {parametro.moeda(num, )}e igual a {parametro.dobro(num, True)}R$:")
print(f"O metade  de {parametro.moeda(num, )}e igual a {parametro.metade(num, True)}R$:")
print(f"Aumentando 10% de {parametro.moeda(num, )}temos {parametro.aumentar(num, 10, True)}R$: de taxa")
print(f"Diminuindo 10% {parametro.moeda(num, )}temos {parametro.diminuir(num, 10, True)}R$: de desconto")