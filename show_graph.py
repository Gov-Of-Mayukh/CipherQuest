# show_graph.py
import csv
import matplotlib.pyplot as plt

def show_graph(filename):
    try:
        student_name = input("Enter student name to view graph: ").strip()

        present = 0
        absent = 0
        found = False

        with open(filename, "r") as file:
            reader = csv.reader(file)
            for row in reader:
                if len(row) != 3:
                    continue
                name, date, status = row
                if name.lower() == student_name.lower():
                    found = True
                    if status.lower() == "present":
                        present += 1
                    else:
                        absent += 1

        if not found:
            print(f"No records found for {student_name}.\n")
            return

        total = present + absent
        if total == 0:
            print(f"No attendance data available for {student_name}.\n")
            return

        plt.figure(figsize=(4,4))
        plt.title(f"Attendance of {student_name}")
        plt.pie(
            [present, absent],
            labels=["Present", "Absent"],
            autopct="%1.1f%%",
            colors=["#4CAF50", "#FF5252"],
            startangle=90
        )
        plt.show()

    except FileNotFoundError:
        print("No records found. Please add records first.\n")
