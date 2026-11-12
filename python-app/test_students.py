import pytest
import psycopg2

from students import add_student, get_student, average_grade


@pytest.fixture
def conn():
    connection = psycopg2.connect(
        host="localhost",
        database="tp",
        user="postgres",
        password="postgres"
    )

    with connection.cursor() as cur:
        cur.execute("TRUNCATE TABLE students RESTART IDENTITY")

    connection.commit()

    yield connection

    connection.close()


def test_add_and_get_student(conn):
    add_student(conn, "Besma", 15)

    student = get_student(conn, "Besma")

    assert student is not None
    assert student[1] == "Besma"
    assert float(student[2]) == 15.0


def test_get_student_missing(conn):
    student = get_student(conn, "Inconnu")

    assert student is None


def test_moyenne(conn):
    add_student(conn, "Amel", 10)
    add_student(conn, "Karim", 14)

    result = average_grade(conn)

    assert result == 12.0
