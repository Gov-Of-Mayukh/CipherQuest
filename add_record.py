# add_record.py
import csv
from datetime import datetime

def add_record(filename):
    name = input("Enter student name: ")
    date = input("Enter date (DD-MM-YYYY) or press Enter for today: ")
    if not date:
        date = datetime.now().strftime("%d-%m-%Y")

    status = input("Enter status (P for Present / A for Absent): ").strip().upper()
    status = "Present" if status == "P" else "Absent"

    with open(filename, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([name, date, status])

    print(f"Attendance recorded for {name} on {date} as {status}.\n")
