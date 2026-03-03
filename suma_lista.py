from collections.abc import Iterable
from numbers import Real


def suma_lista(valores):
    if valores is None:
        raise TypeError("La entrada no puede ser None.")

    if isinstance(valores, (str, bytes)):
        raise TypeError("La entrada debe ser un iterable de números, no str/bytes.")

    if not isinstance(valores, Iterable):
        raise TypeError("La entrada debe ser un iterable de números.")

    total = 0.0
    count = 0

    for x in valores:
        if not isinstance(x, Real):
            raise TypeError(f"Elemento no numérico detectado: {x!r}")
        total += float(x)
        count += 1

    if count == 0:
        raise ValueError("El iterable no puede estar vacío.")

    return total