import newRunner


student1_name = "Francin"
student1_grade = 1.00
student1_subject = ["Physics", "Chemistry"]

newRunner.print_student_info_function(student1_name, student1_grade, student1_subject)


student = newRunner.Student(name="Francin", grade= 1.00, subject=["Physics", "Chemistry"])
student.print.print_student_method()


class Student:
    def __init__(self, name, grade, subject):
        self.name = name
        self.grade = grade
        self.subject = subject


        def print_student_info(self):
            print(f"{self.name} grade:{self.grade} subject:{self.subject}")

        @staticmethod
        def is_grade_passing(grade):
            return grade <=3.0

if __name__ == "__main__":

    student1 = Student("Francie", 1.00, ["Physics", "Chemistry"])
    student1.print_student_info_method()
    if Student.is_grade_passing(student1.grade):
        print("passed")
    else:
        print("failed")

    student2 = Student("Francin", 2.00, ["Physics", "Chemistry"])
    student2.print_student_info_method()
    if Student.is_grade_passing(student2.grade):
        print("passed")
    else:
        print("failed")

    student3 = Student("Francis", 3.00, ["Physics", "Chemistry"])
    student3.print_student_info_method()
    if Student.is_grade_passing(student3.grade):
        print("passed")
    else:
        print("failed")
