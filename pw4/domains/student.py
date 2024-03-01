import numpy as np

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