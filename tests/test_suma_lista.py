import sys
from pathlib import Path
import pytest

sys.path.append(str(Path(__file__).resolve().parents[1]))

from suma_lista import suma_lista


def test_caso_correcto():
    assert suma_lista([1, 2, 3]) == 7.0


def test_caso_limite_lista_con_ceros():
    assert suma_lista([0, 0, 0]) == 0.0


def test_caso_correcto_decimales():
    assert suma_lista([1.5, 2.5]) == 4.0


def test_caso_error_elemento_no_numerico():
    with pytest.raises(TypeError):
        suma_lista([1, "2", 3])


def test_caso_error_lista_vacia():
    with pytest.raises(ValueError):
        suma_lista([])