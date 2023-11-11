import pytest
import Examen2

# Segunda Prueba para el método ObtieneValencia
def test_obtiene_valencia():
    mi_clase = Examen2.MiClase(None, None, None, None, None)
    resultado = mi_clase.ObtieneValencia(10088)
    assert resultado == 1


# Segunda Prueba Unitaria para el método DivisibleTempo
def test_divisible_tempo():
    mi_clase = Examen2.MiClase(None, None, None, None, None)
    resultado = mi_clase.DivisibleTempo(45)
    assert resultado == [1, 3, 5, 9, 15, 45]


# Segunda Prueba unitaria para el método ObtieneMasBailable
def test_obtiene_mas_bailable_prueba_2():
    mi_clase = Examen2.MiClase(None, None, None, None, None)
    resultado = mi_clase.ObtieneMasBailable([10, 35, 3, 90])
    assert resultado == 90

# Segunda Prueba unitaria para el método VerificaListaCanciones cuando hay un elemento None
def test_verifica_lista_canciones_prueba_2():
    clase = Examen2.MiClase(None, None, None, None, None)
    resultado = clase.VerificaListaCanciones([1, 2, None, 3])
    assert not resultado