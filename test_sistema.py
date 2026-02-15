from sistema import login


# Caso de uso 1:
# Verificar login exitoso
def test_login_exitoso():

    resultado = login("admin", "1234")

    assert resultado == True



# Caso de uso 2:
# Verificar password incorrecto
def test_password_incorrecto():

    resultado = login("admin", "0000")

    assert resultado == False



# Caso de uso 3:
# Verificar usuario incorrecto
def test_usuario_incorrecto():

    resultado = login("usuario", "1234")

    assert resultado == False