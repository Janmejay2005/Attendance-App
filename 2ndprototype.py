import json

class AttendanceApp:
    def __init__(self):
        self.student = {}
        self.load_data()

    def save_data(self):
        with open('students.json', 'w') as file:
            json.dump(self.student, file)

    def load_data(self):
        try:
            with open('students.json', 'r') as file:
                self.student = json.load(file)
        except FileNotFoundError:
            self.student = {}

    def add_student(self):
        name = input("Enter student name: ").strip()
        if name in self.student:
            print(f"{name} is already added.")
        else:
            self.student[name] = []
            self.save_data()
            print(f"Student {name} added successfully.")

    def remove_student(self):
        name = input("Enter student name to remove: ").strip()
        if name in self.student:
            del self.student[name]
            self.save_data()
            print(f"Student {name} removed successfully.")
        else:
            print(f"No student found with the name {name}.")

    def mark_attendance(self):
        if not self.student:
            print("No student available. Please add student first.")
            return
        print("Mark attendance for the following students.")
        for name in self.student:
            while True:
                status = input(f"{name} (y/n): ").strip().lower()
                if status in ['y', 'n']:
                    self.student[name].append('Present' if status == 'y' else 'Absent')
                    break
                else:
                    print("Invalid input. Please enter 'y' or 'n'.")
        self.save_data()
        print("Attendance marked successfully.")

    def view_attendance(self):
        if not self.student:
            print("No student available. Please add student first.")
            return
        print("Attendance Records:")
        for name, records in self.student.items():
            print(f"{name}: {','.join(records) if records else 'No record yet'}")

    def menu(self):
        while True:
            print("\nAttendance App Menu:")
            print("1. Add Student")
            print("2. Remove Student")
            print("3. Mark Attendance")
            print("4. View Attendance")
            print("5. Exit")
            choice = input("Enter your choice: ").strip()
            if choice == '1':
                self.add_student()
            elif choice == '2':
                self.remove_student()
            elif choice == '3':
                self.mark_attendance()
            elif choice == '4':
                self.view_attendance()
            elif choice == '5':
                print("Exiting the Attendance App. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    app = AttendanceApp()
    app.menu()
