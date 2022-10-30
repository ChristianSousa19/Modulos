def leiadinhero(msg):
    valido=False
    while not valido:
        entrada=str(input(msg)).replace(",",".").strip()
        if entrada.isalpha():
            print(f"\033[0;31mERRO! {entrada} e um preço invalido\033[m")
        else:
            valido=True
            return float(entrada)
