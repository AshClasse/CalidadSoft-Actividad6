import pytest
from academic_planner import Subject, Student, simulate_semester


# ==============================
# CASO DE USO 1
# Registro de Materias
# ==============================

def test_register_subject_with_prerequisites_met():
    student = Student()
    student.approve_subject("Matemática I")

    calculus = Subject("Cálculo I", 4, ["Matemática I"])

    student.register_subject(calculus)

    assert "Cálculo I" in student.current_subjects


def test_register_subject_without_prerequisites():
    student = Student()

    calculus = Subject("Cálculo I", 4, ["Matemática I"])

    with pytest.raises(Exception):
        student.register_subject(calculus)


# ==============================
# CASO DE USO 2
# Simulación de Trayectoria
# ==============================

def test_simulate_semester_within_credit_limit():
    subjects = [
        Subject("Cálculo I", 4),
        Subject("Física I", 4),
        Subject("Programación I", 3)
    ]

    semester = simulate_semester(subjects, max_credits=8)

    assert len(semester) == 2
    assert "Programación I" not in semester


def test_simulate_semester_exact_credit_limit():
    subjects = [
        Subject("Cálculo I", 4),
        Subject("Física I", 4)
    ]

    semester = simulate_semester(subjects, max_credits=8)

    assert len(semester) == 2
