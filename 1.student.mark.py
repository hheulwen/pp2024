# Student mark management

# Function to input number of students
def noStudent():
    return int(input("Number of students: "))

# Function to append student
def studentInfo():
    # create an empty list to store students
    students = []

    # get the number of students
    num_students = noStudent()

    # information of each student is stored in a dict then dict is appended to students list
    for _ in range(num_students): # using throwaway variable '_' which is not needed for the loop
        student_id = input("Student ID: ")
        student_name = input("Name: ")
        student_dob = input("DoB: ")      
        student = {"ID": student_id, "Name": student_name, "DoB": student_dob}
        students.append(student)
    return students

# Function to list students
def studentList(students):
    for student in students:
        print(f"ID: {student['ID']} - Name: {student['Name']} - DOB: {student['DoB']}")

# Function to input number of courses
def noCourse():
    return int(input("Number of courses: "))

# Function to append course
def courseInfo():
    # create an empty list to store courses
    courses = []

    # get the number of courses
    num_courses = noCourse()

    # information of each course is stored in a dict then dict is appended to courses list
    for _ in range(num_courses):
        course_id = input("Course ID: ")
        course_name = input("Name: ")
        course = {"ID": course_id, "Name": course_name}
        courses.append(course)
    return courses

# Function to list courses
def courseList(courses):
    for course in courses:
        print(f"ID: {course['ID']} - Name: {course['Name']}")

# Function to select a course, input marks for a student in that course
def studentMark(students, courses, marks):
    while True:
        # print all existing courses
        print("Select a course: ")
        courseList(courses)
        
        # enter course id and check if that course exists
        selected_course_ID = input("Enter course ID (or type '0' to finish): ")
        if selected_course_ID == '0':
            break

        # using next() to find selected course in courses list
        # if found, 'selected_course' will refer to that course
        # otherwise, set to None
        selected_course = next((course for course in courses if course['ID'] == selected_course_ID), None)

        # if selected_course exists
        if selected_course:
            while True:
                selected_student_ID = input("Enter student ID to input mark (or type '0' to finish): ")
                if selected_student_ID == '0':
                    break
                
                # find selected student in students list
                selected_student = next((student for student in students if student['ID'] == selected_student_ID), None)

                # if selected_student exists
                if selected_student:
                    mark = input("Enter mark: ")
                    data = {"ID": selected_student['ID'], "Name": selected_student['Name'], "Course": selected_course['Name'], "Mark": mark}
                    marks.append(data)
                    print("Successfully added!")
                else:
                    print("Invalid student ID!")
        else:
            print("Course's not found!")

# Function to list marks for a course
def listMark(course_name, marks):
    print(f"All marks of course {course_name}:")
    for i in marks:
        if i['Course'] == course_name:
            print(f"ID: {i['ID']} - Name: {i['Name']} - Mark: {i['Mark']}")

if __name__ == '__main__':
    marks = []
    students = []
    courses = []
    while True:
        print("--------- Marks management system ---------\n")
        print("Options:\n")
        print("1. Add student's information\n")
        print("2. Add course's information\n")
        print("3. Add student's mark\n")
        print("4. List all students\n")
        print("5. List all courses\n")
        print("6. Show all marks of a course\n")
        print("7. Exit\n")
        opt = int(input("Enter your option: "))
        if opt == 1:
            students = studentInfo()
        if opt == 2:
            courses = courseInfo()
        if opt == 3:
            studentMark(students, courses, marks)
        if opt == 4:
            studentList(students)
        if opt == 5:
            courseList(courses)
        if opt == 6:
            course_name = input("Enter course name to show mark: ")
            listMark(course_name, marks)
        if opt == 7:
            break
        else:
            print("--------------- Completed --------------\n")
