from utilidadescev import Forma

num=float(input("Digite o preço R$: "))
print(f"O dobro de {Forma.moeda(num)}e igual a {Forma.dobro(num)}R$:")
print(f"O metade  de {Forma.moeda(num)}e igual a {Forma.dividir(num)}R$:")
print(f"Aumentando 10% de {Forma.moeda(num)}temos {Forma.aumentar(num, 10)}R$: de taxa")
print(f"Diminuindo 10% {Forma.moeda(num)}temos {Forma.diminuir(num, 10)}R$: de desconto")