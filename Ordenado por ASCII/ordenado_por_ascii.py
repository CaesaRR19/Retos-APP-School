def peso_ascii(text: str) -> int:
    return sum(ord(x) for x in text)


def ordenar_por_ascii():
    diccionario_ascii = {}
    try:
        cantidad = int(input())
    except ValueError:
        print("Ingrese una cantidad válida.")
        return
    for _ in range(cantidad):
        representacion_ascii = input()
        diccionario_ascii[representacion_ascii] = peso_ascii(representacion_ascii)
    ascii_ordenado = sorted(diccionario_ascii.items(), key=lambda item: item[1])
    print()
    for llave in ascii_ordenado:
        print(f"{llave[0]}")


ordenar_por_ascii()
