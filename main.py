import sqlite3

try:
    conn = sqlite3.connect('student_info.db')
    cursor = conn.cursor()
    print('it got it')
except sqlite3.Error as e:
    print(f"Database error: {e}")


# Main menu function
def main_menu():
    while True:
        print("\nStudent Information System")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Quit")

        choice = input("Enter your choice (1/2/3/4/5/6): ")

        if choice == '1':
            add_student()
        elif choice == '2':
            view_students()
        elif choice == '3':
            search_student()
        elif choice == '4':
            update_student()
        elif choice == '5':
            delete_student()
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please try again.")


def add_student():
    name = input("Enter student name: ").upper()

    # Automatically generate the student ID
    cursor.execute("SELECT MAX(student_id) FROM students")
    last_id = cursor.fetchone()[0]
    if last_id is None:
        student_id = "1"
    else:
        student_id = str(int(last_id) + 1)

    student_last_name = input("Enter student last name: ").upper()
    student_email = input("Enter student email: ").lower()
    student_number = input("Enter student phone number: ")
    parent_name = input("Enter parent name: ").upper()
    parent_last_name = input("Enter parent last name: ").upper()
    parent_email = input("Enter parent email: ").lower()
    parent_phone = input("Enter parent phone number: ")
    year_level = input("Enter year level: ")
    subjects = input("Enter subjects (comma-separated): ").split(",")

    # Insert the student data into the database
    cursor.execute(
        "INSERT INTO students (name, student_id, student_last_name, student_email, student_number, parent_name, parent_last_name, parent_email, parent_phone, year_level, subjects) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
        (name, student_id, student_last_name, student_email, student_number, parent_name, parent_last_name, parent_email, parent_phone, year_level, ",".join(subjects)))
    conn.commit()

    print("Student added successfully! Student ID:", student_id)


def view_students():
    # Execute a SELECT query to fetch all student records from the "students" table
    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()

    if not students:
        print("No students found.")
    else:
        print("\nList of Students:")
        print(
            "ID\tName\tLast Name\tStudent Email\tStudent Number\tParent Name\tParent Last Name\tParent Email\tParent Phone\tYear Level\tSubjects")
        print("-" * 120)

        for student in students:
            student_id, name, student_last_name, student_id, student_email, student_number, parent_name, parent_last_name, parent_email, parent_phone, year_level, subjects = student
            subjects_list = subjects.split(",") if subjects else []
            print(
                f"{student_id}\t{name}\t{student_last_name}\t{student_email}\t{student_number}\t{parent_name}\t{parent_last_name}\t{parent_email}\t{parent_phone}\t{year_level}\t{', '.join(subjects_list)}")


def search_student():
    print("Search Student:")
    print("1. Search by Student ID")
    print("2. Search by First Name")
    print("3. Search by Last Name")
    print("4. Search by Full Name")

    search_choice = input("Enter your choice (1/2/3/4): ")

    if search_choice == '1':
        student_id = input("Enter student ID: ").upper()
        search_by_id(student_id)
    elif search_choice == '2':
        first_name = input("Enter student first name: ").upper()
        search_by_name(first_name, last_name=False)
    elif search_choice == '3':
        last_name = input("Enter student last name: ").upper()
        search_by_name(last_name, last_name=True)
    elif search_choice == '4':
        full_name = input("Enter student full name: ").upper()
        search_by_full_name(full_name)
    else:
        print("Invalid choice. Please try again.")

def search_by_id(student_id):
    cursor.execute("SELECT * FROM students WHERE student_id=?", (student_id,))
    student = cursor.fetchone()

    if student:
        print("\nStudent Found:")
        print(
            "ID\tName\tLast Name\tStudent Email\tStudent Number\tParent Name\tParent Last Name\tParent Email\tParent Phone\tYear Level\tSubjects")
        print("-" * 120)
        student_id, name, student_last_name, student_id, student_email, student_number, parent_name, parent_last_name, parent_email, parent_phone, year_level, subjects = student
        subjects_list = subjects.split(",") if subjects else []
        print(
            f"{student_id}\t{name}\t{student_last_name}\t{student_email}\t{student_number}\t{parent_name}\t{parent_last_name}\t{parent_email}\t{parent_phone}\t{year_level}\t{', '.join(subjects_list)}")
    else:
        print("Student not found.")


def search_by_name(name, last_name=False):
    if last_name:
        cursor.execute("SELECT * FROM students WHERE student_last_name=?", (name,))
    else:
        cursor.execute("SELECT * FROM students WHERE name=?", (name,))
    students = cursor.fetchall()

    if students:
        print("\nStudent Found:")
        print(
            "ID\tName\tLast Name\tStudent Email\tStudent Number\tParent Name\tParent Last Name\tParent Email\tParent Phone\tYear Level\tSubjects")
        print("-" * 120)
        for student in students:
            student_id, name, student_last_name, student_id, student_email, student_number, parent_name, parent_last_name, parent_email, parent_phone, year_level, subjects = student
            subjects_list = subjects.split(",") if subjects else []
            print(
                f"{student_id}\t{name}\t{student_last_name}\t{student_email}\t{student_number}\t{parent_name}\t{parent_last_name}\t{parent_email}\t{parent_phone}\t{year_level}\t{', '.join(subjects_list)}")
    else:
        print("No students with that name found.")

def search_by_full_name(full_name):
    cursor.execute("SELECT * FROM students WHERE name || ' ' || student_last_name=?", (full_name,))
    students = cursor.fetchall()

    if students:
        print("\nList of Students Matching the Full Name:")
        print(
            "ID\tName\tLast Name\tStudent Email\tStudent Number\tParent Name\tParent Last Name\tParent Email\tParent Phone\tYear Level\tSubjects")
        print("-" * 120)
        for student in students:
            student_id, name, student_last_name, student_email, student_number, parent_name, parent_last_name, parent_email, parent_phone, year_level, subjects = student
            subjects_list = subjects.split(",") if subjects else []
            print(
                f"{student_id}\t{name}\t{student_last_name}\t{student_email}\t{student_number}\t{parent_name}\t{parent_last_name}\t{parent_email}\t{parent_phone}\t{year_level}\t{', '.join(subjects_list)}")
    else:
        print("No students with that full name found.")


def update_student():
    student_id = input("Enter the student ID to update: ").upper()

    # Check if the student exists
    cursor.execute("SELECT * FROM students WHERE student_id=?", (student_id,))
    student = cursor.fetchone()

    if student:
        print("\nCurrent Student Information:")
        print(
            "ID\tName\tLast Name\tStudent Email\tStudent Number\tParent Name\tParent Last Name\tParent Email\tParent Phone\tYear Level\tSubjects")
        print("-" * 120)
        student_id, name, student_last_name, student_id, student_email, student_number, parent_name, parent_last_name, parent_email, parent_phone, year_level, subjects = student
        subjects_list = subjects.split(",") if subjects else []
        print(
            f"{student_id}\t{name}\t{student_last_name}\t{student_email}\t{student_number}\t{parent_name}\t{parent_last_name}\t{parent_email}\t{parent_phone}\t{year_level}\t{', '.join(subjects_list)}")

        print("\nChoose what to update:")
        print("1. Name")
        print("2. Last Name")
        print("3. Student Email")
        print("4. Student Phone Number")
        print("5. Parent Name")
        print("6. Parent Last Name")
        print("7. Parent Email")
        print("8. Parent Phone Number")
        print("9. Year Level")
        print("10. Subjects")
        print("0. Exit")

        choice = input("Enter your choice (0-10): ")

        if choice == '1':
            new_name = input(f"Enter new name (Current: {name}): ").upper()
            cursor.execute("UPDATE students SET name=? WHERE student_id=?", (new_name or name, student_id))
            conn.commit()
            print(f"Student {student_id} name updated successfully.")
        elif choice == '2':
            new_last_name = input(f"Enter new last name (Current: {student_last_name}): ").upper()
            cursor.execute("UPDATE students SET student_last_name=? WHERE student_id=?", (new_last_name or student_last_name, student_id))
            conn.commit()
            print(f"Student {student_id} last name updated successfully.")
        elif choice == '3':
            new_student_email = input(f"Enter new student email (Current: {student_email}): ").lower()
            cursor.execute("UPDATE students SET student_email=? WHERE student_id=?", (new_student_email or student_email, student_id))
            conn.commit()
            print(f"Student {student_id} email updated successfully.")
        elif choice == '4':
            new_student_number = input(f"Enter new student phone number (Current: {student_number}): ")
            cursor.execute("UPDATE students SET student_number=? WHERE student_id=?", (new_student_number or student_number, student_id))
            conn.commit()
            print(f"Student {student_id} phone number updated successfully.")
        elif choice == '5':
            new_parent_name = input(f"Enter new parent name (Current: {parent_name}): ").upper()
            cursor.execute("UPDATE students SET parent_name=? WHERE student_id=?", (new_parent_name or parent_name, student_id))
            conn.commit()
            print(f"Student {student_id} parent name updated successfully.")
        elif choice == '6':
            new_parent_last_name = input(f"Enter new parent last name (Current: {parent_last_name}): ").upper()
            cursor.execute("UPDATE students SET parent_last_name=? WHERE student_id=?", (new_parent_last_name or parent_last_name, student_id))
            conn.commit()
            print(f"Student {student_id} parent last name updated successfully.")
        elif choice == '7':
            new_parent_email = input(f"Enter new parent email (Current: {parent_email}): ").lower()
            cursor.execute("UPDATE students SET parent_email=? WHERE student_id=?", (new_parent_email or parent_email, student_id))
            conn.commit()
            print(f"Student {student_id} parent email updated successfully.")
        elif choice == '8':
            new_parent_phone = input(f"Enter new parent phone number (Current: {parent_phone}): ")
            cursor.execute("UPDATE students SET parent_phone=? WHERE student_id=?", (new_parent_phone or parent_phone, student_id))
            conn.commit()
            print(f"Student {student_id} parent phone number updated successfully.")
        elif choice == '9':
            new_year_level = input(f"Enter new year level (Current: {year_level}): ")
            cursor.execute("UPDATE students SET year_level=? WHERE student_id=?", (new_year_level or year_level, student_id))
            conn.commit()
            print(f"Student {student_id} year level updated successfully.")
        elif choice == '10':
            new_subjects = input(f"Enter new subjects (comma-separated) (Current: {', '.join(subjects_list)}): ").split(",")
            cursor.execute("UPDATE students SET subjects=? WHERE student_id=?", (",".join(new_subjects) or subjects, student_id))
            conn.commit()
            print(f"Student {student_id} subjects updated successfully.")
        elif choice == '0':
            print("Update canceled.")
        else:
            print("Invalid choice. Please try again.")
    else:
        print(f"Student {student_id} not found.")


def delete_student():
    student_id = input("Enter the student ID to delete: ")

    # Check if the student exists
    cursor.execute("SELECT * FROM students WHERE student_id=?", (student_id,))
    student = cursor.fetchone()

    if student:
        confirm = input(f"Are you sure you want to delete student {student_id}? (yes/no): ").lower()

        if confirm == "yes":
            # Delete the student from the database
            cursor.execute("DELETE FROM students WHERE student_id=?", (student_id,))
            conn.commit()
            print(f"Student {student_id} deleted successfully.")
        else:
            print("Deletion canceled.")
    else:
        print(f"Student {student_id} not found.")


if __name__ == "__main__":
    main_menu()

conn.close()
