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