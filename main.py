import uteis
def fatorial(n):
     f=1
     for c in range(1,n+1):
            f*=c
     return f


def dobro(n):

    return n*2
num=int(input("Digite um numero para ver seu fatorial:"))
fat=fatorial(num)
print(f" fatorial de {num} e igual a {fat} ")