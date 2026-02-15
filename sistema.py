def login(usuario, password):

    usuario_valido = "admin"
    password_valido = "1234"

    if usuario == usuario_valido and password == password_valido:

        return True

    else:

        return False