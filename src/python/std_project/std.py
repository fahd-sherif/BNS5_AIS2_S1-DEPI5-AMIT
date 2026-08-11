class Student:
    _id_counter = 1 #class attribute 
    def __init__(self,name):
        self.student_id = Student._id_counter
        Student._id_counter += 1
        self.name = name
        self.grades = {}
        self.enrolled_courses = []
    def __str__(self):
        return f"Student ID: {self.student_id}, Name: {self.name}, Enrolled Courses: {self.enrolled_courses}, Grades: {self.grades}"

    def __repr__(self) -> str:
        return f"Student ID ({self.student_id}, {self.name}, Enrolled Courses: {self.enrolled_courses}, Grades: {self.grades})"

    def add_grade(self, course_id, grade):
        if not   0<= grade <= 100:
            raise ValueError("Grade must be between 0 and 100.")
        self.grades[course_id] = grade

    def enroll_course(self, course_id):
        if course_id  in self.enrolled_courses:
            raise ValueError(f"Student is already enrolled in course {course_id}.")
        else:
            self.enrolled_courses.append(course_id)