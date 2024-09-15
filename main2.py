# Function to update student marks in both dictionary and file
def update_student_record(student_dict, name, new_marks):
    if name in student_dict:
        student_dict[name] = new_marks
        with open("My_student_Recode.txt", "r+") as f:
            lines = f.readlines()
            f.seek(0)
            for line in lines:
                if line.startswith(name):
                    f.write(f"{name}: {new_marks}\n")
                else:
                    f.write(line)
            f.truncate()
        print("Marks updated successfully.")
    else:
        print(f"Student '{name}' not found.")

# Main program
student = {}

print("\n\n...................You can store the student data in a separate File...............\n")
while True:
    print("Options:")
    print("1. Add Student")
    print("2. Update Student")
    print("3. View Students")
    print("4. Exit")
    try:
        choice = int(input("Enter your choice according to the above options: "))
        
        if choice == 1:
            name = input("Enter the name of the student: ")
            marks = float(input("Enter the marks of the student: "))
            student[name] = marks
            with open("My_student_Recode.txt", "a") as f:
                f.write(f"{name}: {marks}\n")
            print("Student added successfully.")

        elif choice == 2:
            name = input("Enter the name of the student whose marks you want to update: ")
            new_marks = float(input("Enter the new marks: "))
            update_student_record(student, name, new_marks)

        elif choice == 3:
            with open("My_student_Recode.txt") as f:
                print("Student Records:")
                for line in f:
                    print(line.strip())  # strip() removes extra newline characters
                if not student:
                    print("No student records found.")

        elif choice == 4:
            print("Exiting...")
            break

        else:
            print("Invalid Choice. Please enter a number between 1 and 4.")

    except ValueError:
        print("Invalid input. Please enter a valid number.")
