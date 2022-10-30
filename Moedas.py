from utilidadescev import Moeda

num=float(input("Digite o preço R$: "))
print(f"O dobro de {num} R$:  e igual a {Moeda.dobro(num)}R$:")
print(f"O metade  de {num} R$:  e igual a {Moeda.dividir(num)}R$:")
print(f"Aumentando 10% de {num} R$: temos {Moeda.aumentar(num, 10)}R$: de taxa")
print(f"Diminuindo 10% {num} R$: temos {Moeda.diminuir(num, 10)}R$: de desconto")