class Student:
    def __init__(self, name, age, gender, course):
        self.name = name
        self.age = age
        self.gender = gender
        self.course = course
        self.admitted = False

    def admit(self):
        self.admitted = True
        print(f"{self.name} has been admitted to the {self.course} course.")

    def display_info(self):
        admission_status = "Admitted" if self.admitted else "Not Admitted"
        print(f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}, Course: {self.course}, Status: {admission_status}")


class AdmissionProcess:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)
        print(f"Student {student.name} added to the admission list.")

    def process_admissions(self):
        for student in self.students:
            if student.age >= 18:  
                student.admit()
            else:
                print(f"{student.name} is not eligible for admission due to age.")

    def display_all_students(self):
        print("\nAll Students:")
        for student in self.students:
            student.display_info()


class Institute:
    def __init__(self, name):
        self.name = name
        self.admission_process = AdmissionProcess()

    def display_info(self):
        print(f"Welcome to {self.name}!")

    def run_admission_process(self):
        while True:
            print("\n--- Admission Process Menu ---")
            print("1. Add Student")
            print("2. Process Admissions")
            print("3. Display All Students")
            print("4. Exit")
            
            choice = input("Enter your choice (1-4): ")

            if choice == '1':
                name = input("Enter student's name: ")
                age = int(input("Enter student's age: "))
                gender = input("Enter student's gender: ")
                course = input("Enter the course: ")
                student = Student(name, age, gender, course)
                self.admission_process.add_student(student)

            elif choice == '2':
                self.admission_process.process_admissions()

            elif choice == '3':
                self.admission_process.display_all_students()

            elif choice == '4':
                print("Exiting the admission process.")
                break
            
            else:
                print("Invalid choice! Please select a valid option.")


def main():
    institute = Institute("Besant Technologies")
    institute.display_info()
    institute.run_admission_process()


if __name__ == "__main__":
    main()
