import pytest

from students import add_student, average_grade, get_connection, get_student


@pytest.fixture
def conn():
    c = get_connection()
    with c, c.cursor() as cur:
        cur.execute("DELETE FROM students")
    yield c
    c.close()


def test_ajouter_et_lire(conn):
    student_id = add_student(conn, "Amel", 15.5)
    assert get_student(conn, student_id) == {"name": "Amel", "grade": 15.5}


def test_etudiant_inconnu(conn):
    assert get_student(conn, 9999) is None


def test_moyenne(conn):
    add_student(conn, "Amel", 10)
    add_student(conn, "Karim", 14)
    assert average_grade(conn) == 12.0
