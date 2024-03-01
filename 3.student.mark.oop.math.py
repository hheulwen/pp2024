import math
import numpy as np 
import curses

# Student mark management

class Student:
    students = []
    def __init__(self, student_id, student_name, student_dob):
        self.id = student_id
        self.name = student_name
        self.dob = student_dob
        self.gpa = 0
        self.marks = []
        Student.students.append(self) 

    # display student's information
    def studentInfo(self):
        print(f"ID: {self.id} - Name: {self.name} - DOB: {self.dob}")

    def addMark(self, mark):
        self.marks.append(mark)
    
    # calculate GPA
    @classmethod
    def calculateGPA(cls, student_id):
        student = None
        for i in cls.students:
            if i.id == student_id:
                student = i
                break
        
        if not student:
            return 0
        
        # no mark yet
        if not student.marks:
            return 0

        weighted_sum = 0
        total_credits = 0

        for mark in student.marks:
            weighted_sum += mark.mark * mark.course.credit
            total_credits += mark.course.credit

        if total_credits == 0:
            return 0   
        student.gpa = np.divide(weighted_sum, total_credits)
        return student.gpa
        

    # add students
    @classmethod
    def add(cls): 
        student_id = input("Student ID: ")

        # check if student with that ID is already existed
        for student in cls.students:
            if student.id == student_id:
                print("Student with that ID is already existed!")
                return
            
        student_name = input("Name: ")
        student_dob = input("DOB: ")
        student = cls(student_id, student_name, student_dob) 
        print("Successfully added!")

    # list all students
    @classmethod
    def list(cls):
        for student in cls.students:
            student.studentInfo()

class Course:
    courses = []
    def __init__(self, course_id, course_name, credit):
        self.id = course_id
        self.name = course_name
        self.credit = credit
        Course.courses.append(self)

    # display course's information
    def courseInfo(self):
        print(f"Course: {self.name} - ID: {self.id} - Credit: {self.credit}")
    
    # add course
    @classmethod
    def add(cls):
        id = input("Course ID: ")

        # check if a course is already existed
        for course in cls.courses:
            if course.id == id:
                print("Course ID is already existed!")
                return
            
        name = input("Course: ")
        credit = int(input("Credit: "))
        course = cls(id, name, credit)
        print("Successfully added!")

    # list all courses
    @classmethod
    def list(cls):
        for course in cls.courses:
            course.courseInfo()   

class Mark:
    def __init__(self, course, student, mark):
        self.course = course
        self.student = student
        self.mark = mark

    # display mark of a course
    def markInfo(self):
        print(f"ID: {self.student.id} - Name: {self.student.name} - Course: {self.course.name} - Mark: {self.mark}")
        
class markSystem:
    def __init__(self):
        self.marks = []

    # add mark
    def add(self):
        course_id = input("Enter course ID: ")
        student_id = input("Enter student ID: ")

        # check if the mark for the same student and course already exists
        for mark in self.marks:
            if mark.student.id == student_id and mark.course.id == course_id:
                print("Mark for the this student in course is already exists. Cannot add twice!")
                return
            
        mark_data = float(input("Enter mark: "))

        # round down score to 1-digit decimal
        rounded = math.floor(mark_data * 10) / 10 

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
            mark = Mark(course, student, rounded)
            student.addMark(mark)
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
        print("7. Show GPA of specific student\n")
        print("8. Sort student list by GPA descending\n ")
        print("9. Exit\n")

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
            print(f'GPA of student {student_id}: {gpa: .2f}')
        elif option == 8:
            sorted_list = sorted(Student.students, key=lambda s:s.gpa, reverse=True)
            for student in sorted_list:
                student.studentInfo()
        elif option == 9:
            break
        else:
            print("Invalid option. Please try again.")

        print("--------------- Completed --------------\n")