


class Student:


    def __init__(self, name, grade, subject):
        self.name =name
        self.grade = grade
        self.subject = subject


    def print_student_info(self):
        print(f"{self.name} grade:{self.grade} subject:{self.subject}")




if __name__ == "__main__":
        student1 = Student(name="Francie", grade= 1.25, subject=["Physics", "Chemistry"])
        student1.print_student_info_method()
        student2 = Student(name="Francin", grade= 1.00, subject=["Physics", "Chemistry"])
        student2.print_student_info_method()
        student3 = Student(name="Francis", grade= 1.75, subject=["Physics", "Chemistry"])
        student3.print_student_info_method()

