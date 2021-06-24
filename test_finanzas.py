import pytest
import finanzas



def test_contar_meses():
    meses = 12
    assert meses == finanzas.contar_meses()

def test_contar_filas():
    filas = 1
    assert finanzas.contar_filas() >= filas

