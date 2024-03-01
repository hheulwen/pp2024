class Mark:
    def __init__(self, course, student, mark):
        self.course = course
        self.student = student
        self.mark = mark

    # display mark of a course
    def markInfo(self):
        print(f"ID: {self.student.id} - Name: {self.student.name} - Course: {self.course.name} - Mark: {self.mark}")