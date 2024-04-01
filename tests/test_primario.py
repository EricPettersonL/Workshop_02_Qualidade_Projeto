from app.funcao import primario

def test_primario():
    saida = primario()
    gabarito = "Função primario"
    assert saida == gabarito