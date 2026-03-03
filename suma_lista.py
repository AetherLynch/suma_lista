from collections.abc import Iterable
from numbers import Real


def suma_lista(valores):
    if valores is None:
        raise TypeError("La entrada no puede ser None.")

    if not isinstance(valores, Iterable) or isinstance(valores, (str, bytes)):
        raise TypeError("La entrada debe ser un iterable válido de números.")

    total = 0.0
    contador = 0

    for elemento in valores:
        if not isinstance(elemento, Real):
            raise TypeError(f"Elemento no numérico detectado: {elemento}")
        total += float(elemento)
        contador += 1

    if contador == 0:
        raise ValueError("La lista no puede estar vacía.")

    return total


if __name__ == "__main__":
    numeros = []

    while True:
        entrada = input("Número (o 'fin' para terminar): ")

        if entrada.lower() == "fin":
            break

        try:
            numero = float(entrada)
            numeros.append(numero)
        except ValueError:
            print("Entrada inválida.")

    try:
        resultado = suma_lista(numeros)
        print("Lista ingresada:", numeros)
        print("Suma total:", resultado)
    except Exception as e:
        print("Error:", e)