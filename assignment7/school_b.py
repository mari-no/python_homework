import sqlite3


def add_student(cursor, name, age, major):
    try:
        cursor.execute(
            "INSERT INTO Students (name, age, major) VALUES (?, ?, ?)",
            (name, age, major)
        )
    except sqlite3.IntegrityError:
        print(f"{name} is already in the database.")


def add_course(cursor, name, instructor):
    try:
        cursor.execute(
            "INSERT INTO Courses (course_name, instructor_name) VALUES (?, ?)",
            (name, instructor)
        )
    except sqlite3.IntegrityError:
        print(f"{name} is already in the database.")


def enroll_student(cursor, student, course):

    # Find student
    cursor.execute(
        "SELECT * FROM Students WHERE name = ?",
        (student,)
    )

    results = cursor.fetchall()

    if len(results) > 0:
        student_id = results[0][0]
    else:
        print(f"There was no student named {student}.")
        return

    # Find course
    cursor.execute(
        "SELECT * FROM Courses WHERE course_name = ?",
        (course,)
    )

    results = cursor.fetchall()

    if len(results) > 0:
        course_id = results[0][0]
    else:
        print(f"There was no course named {course}.")
        return

    # Check if already enrolled
    cursor.execute(
        "SELECT * FROM Enrollments WHERE student_id = ? AND course_id = ?",
        (student_id, course_id)
    )

    results = cursor.fetchall()

    if len(results) > 0:
        print(f"Student {student} is already enrolled in course {course}.")
        return

    # Enroll student
    cursor.execute(
        "INSERT INTO Enrollments (student_id, course_id) VALUES (?, ?)",
        (student_id, course_id)
    )


with sqlite3.connect("../db/school.db") as conn:

    conn.execute("PRAGMA foreign_keys = 1")
    cursor = conn.cursor()

    add_student(cursor, "Jasmine", 20, "Computer Science")
    add_student(cursor, "Pratik", 22, "History")
    add_student(cursor, "Carlos", 19, "Biology")

    add_course(cursor, "Math 101", "Dr. Smith")
    add_course(cursor, "English 101", "Ms. Jones")
    add_course(cursor, "Chemistry 101", "Dr. Lee")

    conn.commit()

    # Enroll students
    enroll_student(cursor, "Jasmine", "Math 101")
    enroll_student(cursor, "Jasmine", "Chemistry 101")
    enroll_student(cursor, "Pratik", "Math 101")
    enroll_student(cursor, "Pratik", "English 101")
    enroll_student(cursor, "Carlos", "English 101")

    conn.commit()