import os

import psycopg2


def get_connection():
    return psycopg2.connect(
        host=os.getenv("DB_HOST", "localhost"),
        port=os.getenv("DB_PORT", "5432"),
        dbname=os.getenv("DB_NAME", "tp"),
        user=os.getenv("DB_USER", "postgres"),
        password=os.getenv("DB_PASSWORD", "postgres"),
    )


def add_student(conn, name, grade):
    """Ajoute un étudiant et retourne son id."""
    with conn, conn.cursor() as cur:
        cur.execute(
            "INSERT INTO students (name, grade) VALUES (%s, %s) RETURNING id",
            (name, grade),
        )
        return cur.fetchone()[0]


def get_student(conn, student_id):
    """Retourne {"name": ..., "grade": ...}, ou None si l'étudiant n'existe pas."""
    with conn, conn.cursor() as cur:
        cur.execute("SELECT name, grade FROM students WHERE id = %s", (student_id,))
        row = cur.fetchone()
        if row is None:
            return None
        return {"name": row[0], "grade": float(row[1])}


def average_grade(conn):
    """Retourne la moyenne des notes, ou None s'il n'y a aucun étudiant."""
    with conn, conn.cursor() as cur:
        cur.execute("SELECT AVG(grade) FROM students")
        value = cur.fetchone()[0]
        return float(value) if value is not None else None
