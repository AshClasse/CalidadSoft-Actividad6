# Pruebas Unitarias - Sistema de Login

## Descripción

Este proyecto implementa pruebas unitarias para un sistema de autenticación utilizando Python y pytest.

El objetivo es validar el correcto funcionamiento del proceso de inicio de sesión.

---

## Framework utilizado

pytest

---

## Casos de uso probados

### Caso de uso 1: Login exitoso

Archivo:

test_login_exitoso

Propósito:

Validar que el sistema permita el acceso con credenciales correctas.

Resultado esperado:

True

---

### Caso de uso 2: Password incorrecto

Archivo:

test_password_incorrecto

Propósito:

Validar que el sistema deniegue el acceso con password incorrecto.

Resultado esperado:

False

---

### Caso de uso 3: Usuario incorrecto

Archivo:

test_usuario_incorrecto

Propósito:

Validar que el sistema deniegue el acceso con usuario incorrecto.

Resultado esperado:

False

---

## Ejecución de pruebas

Instalar pytest:

pip install pytest

Ejecutar:

pytest

Resultado esperado:

3 passed

---

## Autor

Ashley CLasse 