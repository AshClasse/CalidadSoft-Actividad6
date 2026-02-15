Plataforma para Optimización de Trayectorias Académicas
Implementación de Pruebas Unitarias

Estudiante: Ashley Classe
Institución: Universidad Iberoamericana
Asignatura: Calidad y Pruebas de Software

Descripción

Este repositorio contiene la implementación de pruebas unitarias para la Plataforma para Optimización de Trayectorias Académicas.

El objetivo es validar la correcta funcionalidad de la lógica académica del sistema, específicamente:

Registro de materias con validación de prerrequisitos

Simulación de semestre respetando límite de créditos

Las pruebas fueron desarrolladas utilizando pytest en Python.

Casos de Uso Cubiertos
Registro de Materias

Permite registrar materias cuando se cumplen prerrequisitos.

Bloquea el registro si no se cumplen.

Maneja excepciones correctamente.

Simulación Académica

Controla el límite máximo de créditos.

Valida escenarios límite (boundary testing).

Garantiza estabilidad en el cálculo de carga académica.

Tecnologías Utilizadas

Python

pytest

Git

Ejecución

Instalar dependencias:

pip install -r requirements.txt


Ejecutar pruebas:

pytest

Propósito Académico

Este proyecto demuestra la aplicación de pruebas unitarias para asegurar calidad, detección temprana de errores y validación de reglas de negocio en un sistema académico.
