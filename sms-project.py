import mysql.connector

# =========== CONNECT TO MYSQL ===================
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123456789"
)

cur = conn.cursor()

# =========== CREATE DATABASE =====================
cur.execute("CREATE DATABASE IF NOT EXISTS studentdb")
cur.execute("USE studentdb")

# ===========CREATE TABLE ========================
cur.execute()
conn.commit()


# 1. =========== ADD STUDENT ===================
def add_student():
    id = input("ID: ")
    name = input("Name: ")
    course = input("Course: ")
    marks = input("Marks: ")

    
    cur.execute("INSERT INTO students VALUES(%s, %s, %s, %s)", 
                    (id, name, course, marks))
    conn.commit()
    print("Student added!\n")

    # print("Error: ID already exists!\n")


# 2.========= VIEW STUDENTS===========================
def view_students():
    cur.execute("SELECT * FROM students")
    data = cur.fetchall()

    if not data:
        print("No records!\n")
        return

    for row in data:
        print(row)
    # print()


# 3. ========= UPDATE STUDENT =====================
def update_student():
    id = input("Enter ID to update: ")

    name = input("New Name: ")
    course = input("New Course: ")
    marks = input("New Marks: ")

    cur.execute(
        UPDATE students 
        SET name=%s, course=%s, marks=%s 
        WHERE id=%s
    , (name, course, marks, id))

    conn.commit()
    print("Updated!\n")


# 4.======= DELETE STUDENT=====================
def delete_student():
    id = input("Enter ID to delete: ")

    cur.execute("DELETE FROM students WHERE id=%s", (id,))
    conn.commit()
    print("Deleted!\n")


# =========== MENU =========================
while True:
    print("1. Add Student")
    print("2. View Students")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Choose: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        update_student()
    elif choice == "4":
        delete_student()
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice!\n")

conn.close()