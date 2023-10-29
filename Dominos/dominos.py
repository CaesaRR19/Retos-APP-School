MENSAJE_ERROR = "Por favor, ingrese fichas válidas."


def puede_ganar():
    try:
        juego_completo = list(map(int, input().split(" ")))
    except ValueError:
        print(MENSAJE_ERROR)
        return

    #! Esta parte comprueba que se los datos estén correctos.
    # * (Que se envien 4 valores y que cada dato esté en el rango de 1 y 6).
    if len(juego_completo) == 4 and all(x in range(1, 7) for x in juego_completo):
        fichas_fito, fichas_tablero = juego_completo[:2], juego_completo[2:]
        for ficha in fichas_fito:
            if ficha in fichas_tablero:
                print("SI")
                return
        print("NO")
    else:
        print(MENSAJE_ERROR)


puede_ganar()
