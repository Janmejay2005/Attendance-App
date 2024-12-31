class AttendanceApp:
    def __init__(self):
        self.student = {} 
    def add_student(self):
        name = input("Enter student name: ").strip()
        if name in self.student:
            print(f"{name} is already added.")
        else:
            self.student[name] = []
            print(f"Student {name} added successfully.")
    def mark_attendance(self):
        if not self.student:
            print("No student available. Please add student first.")
            return
        print("Mark attendance for the following students.")
        for name in self.student:
            status = input(f"{name} (y/n): ").strip().lower()
            if status == 'y':
                self.student[name].append('Present')
            else:
                self.student[name].append('Absent')
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
            print("2. Mark Attendance")
            print("3. View Attendance")
            print("4. Exit")
            choice = input("Enter your choice: ").strip()
            if choice == '1':
                self.add_student()
            elif choice == '2':
                self.mark_attendance()
            elif choice == '3':
                self.view_attendance()
            elif choice == '4':
                print("Exiting the Attendance App. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")       
if __name__ == "__main__":
    app = AttendanceApp()
    app.menu()
