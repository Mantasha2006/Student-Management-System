students ={}

while True:
    print("......Student Management System.......")
    print("1.Add Student")
    print("2.View All Student")
    print("3.Search Student")
    print("4.Delete Student")
    print("5.Exit")

    choice = input("Enter your choice:")

    if choice== "1":
        student_id =input("Enter Student ID:")

        if student_id in students:
            print("Stude ID already exist.")

        else:
            name = input("Enter student name:")
            Age =int(input("Enter student Age:")) 
            Course = input("Enter course name:")
            Marks = int(input("Enter student marks:"))      
            
            students[student_id]={
                "name":name,
                "Age":Age,
                "Course":Course,
                "Marks":Marks
            }

            print("Student record added successfully!")

    elif choice == "2":
        if not students:
            print("Student ID not found.")

        else:
            for student_id, details in students.items():
                print("Student ID",student_id)
                print("Name",details["name"])
                print("Age",details["Age"])
                print("Course",details["Course"])
                print("Marks",details["Marks"])

    elif choice== "3":
        student_id =input("Enter Student ID:")

        if student_id in students:
            details =students[student_id]

            print("Student Found")
            print("Name",details["name"])
            print("Age",details["Age"])
            print("Course",details["Course"])
            print("Marks",details["Marks"])

        else:
            print("Student not found")

    elif choice== "4":
        if student_id in students:
            del students[student_id]
            print("Student deleted successfully!")

        else:
            print("Student not found.")

    elif choice== "5":
        print("Thankyou for using student mangement system!!!")
        break
    else:
        print("Invalid choice")


    