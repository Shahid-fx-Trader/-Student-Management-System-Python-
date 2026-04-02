class Student:
    all_students = []
    def __init__(self, name, marks, roll_no):
        self.name = name
        self.marks = marks
        self.roll_no = roll_no

    @classmethod
    def add_Student(cls):
        name = input("Enter student name: ")
        marks = int(input("Enter student marks: "))
        roll_no = int(input("Enter student roll number: "))
        student = cls(name, marks, roll_no)
        cls.all_students.append(student)
        print(f"Student {name} added successfully!")

    @classmethod
    def update_Student(cls):
        roll = int(input("Enter the roll number of the student to update: "))
        for student in cls.all_students:
            if student.roll_no == roll:
                new_name = input("Enter new name: ")
                new_marks = int(input("Enter new marks: "))
                student.name = new_name
                student.marks = new_marks
                print(f"Student with roll number {roll} updated successfully!")
                return
        print(f"No student found with roll number {roll}.")

    @classmethod
    def view_Students(cls):
        by_roll_no = int(input("Enter the roll number of the student to view: "))
        for student in cls.all_students:
            if student.roll_no == by_roll_no:
                print(f"Name: {student.name}, Marks: {student.marks}, Roll No: {student.roll_no}")
                return
        print(f"No student found with roll number {by_roll_no}.")

def Menu():
    while True:
        print("\n ====== Student Management System ======")
        print("1. Add Student")
        print("2. View Students")
        print("3. Update Student")
        print("4. Exit")

        choice = int(input("Enter your choice option between 1-4: "))
        if choice == 1:
            Student.add_Student()
        elif choice == 2:
            Student.view_Students()
        elif choice == 3:
            Student.update_Student()
        elif choice == 4:
            print("😊👋 Exiting the program. Goodbye!👋😊")
            print("PROGRAM IS ENDING...")
            print("Made with ❤️  by [Shahid Khan] follow me on github and linkedin")
            print("😎 GitHub: https://github.com/Shahid-fx-Trader 😎")
            print("😎 LinkedIn: linkedin.com/in/shahid-khan-trader 😎")
            print("🎯 Follow me on LinkedIn and send a (connection) request! 🎯")
            print("🎯 Thank you for using the Student Management System. Have a great day! 🌟")
            exit()



if __name__ == "__main__":
    Menu()