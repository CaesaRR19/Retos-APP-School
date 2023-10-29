MENSAJE_ERROR = "Por favor, ingrese un número válido."


def suma_impares():
    try:
        numeros = int(input())
    except ValueError:
        print(MENSAJE_ERROR)
    if numeros in range(1, 110):
        result = 0
        for n in range(1, numeros * 2 + 1, 2):
            result += n % 10
        print(result)
    else:
        print(MENSAJE_ERROR)


suma_impares()
