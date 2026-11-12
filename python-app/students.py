import psycopg2


def add_student(conn, name, grade):
    with conn.cursor() as cur:
        cur.execute(
            "INSERT INTO students (name, grade) VALUES (%s, %s)",
            (name, grade)
        )


def get_student(conn, name):
    with conn.cursor() as cur:
        cur.execute(
            "SELECT id, name, grade FROM students WHERE name = %s",
            (name,)
        )
        return cur.fetchone()


def average_grade(conn):
    with conn.cursor() as cur:
        cur.execute("SELECT AVG(grade) FROM students")
        result = cur.fetchone()

        if result[0] is None:
            return 0.0

        return float(result[0])