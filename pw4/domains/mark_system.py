import math
import numpy as np
from domains.course import Course
from domains.student import Student
from domains.mark import Mark

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