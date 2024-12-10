class Student:
    def __init__(self, name, degree):
        self.name = name
        self.degree = degree

    def main(self):
        student = self.get_student()
        print(f"{student.name} from {student.degree}")

    def get_student(self):
        self.name = input("Name: ")
        self.degree = input("degree: ")
        student = Student(self.name, self.degree)
        return student
    

if __name__ == "__main__":
    student = Student("", "")
    student.main()