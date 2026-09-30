students = []

while True:
    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student name ")
    print("2. Display Students here")
    print("3. Search Student")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    # Add Student
    if choice == 1:
        name = input("Enter student name: ")
        roll_no = int(input("Enter roll number: "))

        marks = []

        for i in range(1, 6):
            mark = int(input(f"Enter marks of subject {i}: "))
            marks.append(mark)

        total = sum(marks)
        percentage = total / 5

        if percentage >= 80:
            grade = "A"
        elif percentage >= 60:
            grade = "B"
        elif percentage >= 40:
            grade = "C"
        else:
            grade = "Fail"

        student = {
            "name": name,
            "roll_no": roll_no,
            "marks": marks,
            "total": total,
            "percentage": percentage,
            "grade": grade
        }

        students.append(student)

        print("Student added successfully!")

    # Display Students
    elif choice == 2:

        if len(students) == 0:
            print("No students found.")

        else:
            print("\n===== ALL STUDENTS =====")

            for student in students:
                print("\nName:", student["name"])
                print("Roll No:", student["roll_no"])
                print("Marks:", student["marks"])
                print("Total:", student["total"])
                print("Percentage:", student["percentage"])
                print("Grade:", student["grade"])

    # Search Student
    elif choice == 3:

        roll_no = int(input("Enter roll number to search: "))

        found = False

        for student in students:

            if student["roll_no"] == roll_no:
                print("\n===== STUDENT FOUND =====")
                print("Name:", student["name"])
                print("Roll No:", student["roll_no"])
                print("Marks:", student["marks"])
                print("Total:", student["total"])
                print("Percentage:", student["percentage"])
                print("Grade:", student["grade"])

                found = True

        if found == False:
            print("Student not found.")

    # Exit
    elif choice == 4:
        print("Thank you!")
        break

    else:
        print("Invalid choice!")