from input import user
from output import display
from domains.student import Student
from domains.course import Course
from domains.mark_system import markSystem

if __name__ == '__main__':
    mark_system = markSystem()

    while True:
        display("--------- Marks Management System ---------\n")
        display("Options:\n")
        display("1. Add student's information\n")
        display("2. Add course's information\n")
        display("3. Add student's mark\n")
        display("4. List all students\n")
        display("5. List all courses\n")
        display("6. Show all marks\n")
        display("7. Show GPA of specific student\n")
        display("8. Sort student list by GPA descending\n ")
        display("9. Exit\n")

        option = int(input("Enter your option: "))

        if option == 1:
            Student.add()  
        elif option == 2:
            Course.add()   
        elif option == 3:
            mark_system.add()  
        elif option == 4:
            Student.list()
        elif option == 5:
            Course.list()
        elif option == 6:
            for mark in mark_system.marks:
                mark.markInfo()
        elif option == 7:
            student_id = input("Enter student ID: ")
            gpa = Student.calculateGPA(student_id)
            display(f'GPA of student {student_id}: {gpa: .2f}')
        elif option == 8:
            sorted_list = sorted(Student.students, key=lambda s:s.gpa, reverse=True)
            for student in sorted_list:
                student.studentInfo()
        elif option == 9:
            break
        else:
            display("Invalid option. Please try again.")

        display("--------------- Completed --------------\n")