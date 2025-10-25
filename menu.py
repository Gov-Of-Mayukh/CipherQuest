# menu.py
import add_record
import view_records
import calculate_percentage
import show_graph
import os

FILENAME = "attendance.csv"

def create_file_if_not_exists():
    if not os.path.exists(FILENAME):
        with open(FILENAME, "w", newline="") as file:
            pass

def menu():
    create_file_if_not_exists()
    while True:
        print("===== STUDENT ATTENDANCE SYSTEM =====")
        print("1. Mark Attendance")
        print("2. View Attendance Records")
        print("3. View Attendance Percentage")
        print("4. Show Attendance Graph")
        print("5. Exit")


        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            add_record.add_record(FILENAME)
        elif choice == "2":
            view_records.view_records(FILENAME)
        elif choice == "3":
            calculate_percentage.calculate_percentage(FILENAME)
        elif choice == "4":
            show_graph.show_graph(FILENAME)
        elif choice == "5":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice! Try again.\n")

if __name__ == "__main__":
    menu()
