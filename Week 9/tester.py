class Student:
    def __init__(self, name, grade, subject):
        self.name = name
        self.grade = grade
        self.subject = subject

    # Corrected Indentation (Method is now part of the class)
    def print_student_info(self):
        print(f"{self.name} grade:{self.grade} subject:{self.subject}")

    @staticmethod
    def is_grade_passing(grade):
        # Assumes a lower number is a better/passing grade
        return grade <= 3.0

if __name__ == "__main__":

    student1 = Student("Francie", 1.00, ["Physics", "Chemistry"])
    student1.print_student_info() # Corrected call
    if Student.is_grade_passing(student1.grade):
        print("passed")
    else:
        print("failed")

    student2 = Student("Francin", 2.00, ["Physics", "Chemistry"])
    student2.print_student_info() # Corrected call
    if Student.is_grade_passing(student2.grade):
        print("passed")
    else:
        print("failed")

    student3 = Student("Francis", 3.00, ["Physics", "Chemistry"])
    student3.print_student_info() # Corrected call
    if Student.is_grade_passing(student3.grade):
        print("passed")
    else:
        print("failed")