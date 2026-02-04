# Coaching Management System
# Language: Python
# Database: SQLite
# Author: Your Name

import sqlite3

# Database connect
conn = sqlite3.connect("coaching.db")
cursor = conn.cursor()

# Tables
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    phone TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS payments (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id INTEGER,
    amount INTEGER,
    date TEXT
)
""")

conn.commit()

# Add student
def add_student():
    name = input("Student name: ")
    phone = input("Phone: ")

    cursor.execute(
        "INSERT INTO students (name, phone) VALUES (?,?)",
        (name, phone)
    )
    conn.commit()
    print("Student added")

# Add payment
def add_payment():
    sid = input("Student ID: ")

    # STEP 2 CHECK (YAHI ADD KARNA THA)
    cursor.execute("SELECT id FROM students WHERE id=?", (sid,))
    if not cursor.fetchone():
        print("Student ID not found")
        return

    amount = input("Amount: ")
    date = input("Date (YYYY-MM-DD): ")

    cursor.execute(
        "INSERT INTO payments (student_id, amount, date) VALUES (?,?,?)",
        (sid, amount, date)
    )
    conn.commit()
    print("Payment added")
    
    
# Monthly report
def monthly_report():
    month = input("Month (MM): ")

    cursor.execute(
        "SELECT SUM(amount) FROM payments WHERE substr(date,6,2)=?",
        (month,)
    )
    total = cursor.fetchone()[0]
    print("Total collection:", total if total else 0)

def show_students():
    cursor.execute("SELECT * FROM students")
    data = cursor.fetchall()

    if not data:
        print("No students found")
    else:
        for s in data:
            print(s)
            
            
# Menu
while True:
    print("\n1 Add Student")
    print("2 Add Payment")
    print("3 Monthly Report")
    print("4 Exit")
    print("5 Show Students")

    ch = input("Choose: ")

    if ch == "1":
        add_student()
    elif ch == "2":
        add_payment()
    elif ch == "3":
        monthly_report()
    elif ch=="5":
        show_students()
    elif ch == "4":
        print("Thankyou for using coaching manager")
        break
    else:
        print("Wrong choice")
