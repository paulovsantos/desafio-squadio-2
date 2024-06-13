def classificar_numero(numero):
    if numero > 0:
        return "positivo"
    elif numero < 0:
        return "negativo"
    else:
        return "zero"


def main():
    positivos = 0
    negativos = 0

    while True:
        numero = int(input("Digite um número (0 para parar): "))

        if numero == 0:
            break

        if numero > 0:
            positivos += 1
        elif numero < 0:
            negativos += 1

        print(classificar_numero(numero))

    print(f"{positivos} números positivos, {negativos} números negativos")


if __name__ == "__main__":
    main()
