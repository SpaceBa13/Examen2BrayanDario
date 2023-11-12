import Examen2


# Prueba para el método ObtieneValencia
def test_obtiene_valencia():
    mi_clase = Examen2.MiClase(None, None, None, None, None)
    resultado = mi_clase.ObtieneValencia(55522)
    assert resultado == 3

# Prueba para el método DivisibleTempo
def test_divisible_tempo():
    mi_clase = Examen2.MiClase(None, None, None, None, None)
    resultado = mi_clase.DivisibleTempo(15)
    assert resultado == [1, 3, 5, 15]


# Prueba para el método ObtieneMasBailable
def test_obtiene_mas_bailable():
    mi_clase = Examen2.MiClase(None, None, None, None, None)
    resultado = mi_clase.ObtieneMasBailable([0.2, 0.1, 0.5, 0.3])
    assert resultado == 0.6


# Prueba para el método VerificaListaCanciones
def test_verifica_lista_canciones():
    mi_clase = Examen2.MiClase(None, None, None, None, None)
    resultado = mi_clase.VerificaListaCanciones(["Rock Thing", "Deadlocked", "Hydra"])
    assert resultado

# Segunda Prueba para el método ObtieneValencia
def test_obtiene_valencia2():
    mi_clase = Examen2.MiClase(None, None, None, None, None)
    resultado = mi_clase.ObtieneValencia(10088)
    assert resultado == 1


# Segunda Prueba Unitaria para el método DivisibleTempo
def test_divisible_tempo2():
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

# Prueba unitaria para el método Encuentra
def test_encuentra():
    mi_clase = Examen2.MiClase(None, None, None, None, None)
    resultado = mi_clase.Encuentra([10, 35, 3, 90], 90)
    assert resultado
