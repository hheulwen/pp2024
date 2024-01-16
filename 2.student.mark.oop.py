# OOP'ed student mark management
class Student:
    students = []
    # constructor
    def __init__(self, student_id, student_name, student_dob):
        self.id = student_id
        self.name = student_name
        self.dob = student_dob
        Student.students.append(self) # add each instance 

    # method to display student's information
    def studentInfo(self):
        print(f"ID: {self.id} - Name: {self.name} - DOB: {self.dob}")

    # method to add students
    @classmethod
    def add(cls): # cls parameter is used to refer to class itself within class method
        student_id = input("Student ID: ")

        # check if student with that ID is already existed
        for student in cls.students:
            if student.id == student_id:
                print("Student with that ID is already existed!")
                return
            
        student_name = input("Name: ")
        student_dob = input("DOB: ")
        student = cls(student_id, student_name, student_dob) # cls is a constructor function
        # it will construct class Student and call the __init__
        print("Successfully added!")

    # method to list all students
    @classmethod
    def list(cls):
        for student in cls.students:
            student.studentInfo()

class Course:
    courses = []
    # constructor
    def __init__(self, course_id, course_name):
        self.id = course_id
        self.name = course_name
        Course.courses.append(self)

    # method to display course's information
    def courseInfo(self):
        print(f"Course: {self.name} - ID: {self.id}")
    
    # method to add course
    @classmethod
    def add(cls):
        id = input("Course ID: ")

        # check if a course is already existed
        for course in cls.courses:
            if course.id == id:
                print("Course ID is already existed!")
                return
            
        name = input("Course: ")
        course = cls(id, name)
        print("Successfully added!")

    # method to list all courses
    @classmethod
    def list(cls):
        for course in cls.courses:
            course.courseInfo()   

class Mark:
    # constructor
    def __init__(self, course, student, mark):
        self.course = course
        self.student = student
        self.mark = mark

    # method to display mark of a course
    def markInfo(self):
        print(f"ID: {self.student.id} - Name: {self.student.name} - Course: {self.course.name} - Mark: {self.mark}")
        
class markSystem:
    def __init__(self):
        self.marks = []
    # method to add mark
    def add(self):
        course_id = input("Enter course ID: ")
        student_id = input("Enter student ID: ")

        # check if the mark for the same student and course already exists
        for mark in self.marks:
            if mark.student.id == student_id and mark.course.id == course_id:
                print("Mark for the this student in course is already exists. Cannot add twice!")
                return
            
        mark_data = input("Enter mark: ")

        # find course object
        course = None
        for i in Course.courses:
            if i.id == course_id:
                course = i
                break

        # find student object
        student = None
        for i in Student.students:
            if i.id == student_id:
                student = i
                break
        
        if student and course:
            mark = Mark(course, student, mark_data)
            self.marks.append(mark)
            print("Successfully added!")
        else: 
            print ("Cannot find student ID or course ID!")

if __name__ == '__main__':
    mark_system = markSystem()

    while True:
        print("--------- Marks Management System ---------\n")
        print("Options:\n")
        print("1. Add student's information\n")
        print("2. Add course's information\n")
        print("3. Add student's mark\n")
        print("4. List all students\n")
        print("5. List all courses\n")
        print("6. Show all marks\n")
        print("7. Exit\n")

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
            break
        else:
            print("Invalid option. Please try again.")

        print("--------------- Completed --------------\n")