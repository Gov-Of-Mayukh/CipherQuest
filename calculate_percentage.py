# calculate_percentage.py
import csv

def calculate_percentage(filename):
    try:
        data = {}
        with open(filename, "r") as file:
            reader = csv.reader(file)
            for row in reader:
                if len(row) != 3:
                    continue
                name, date, status = row
                if name not in data:
                    data[name] = {"Present": 0, "Total": 0}
                data[name]["Total"] += 1
                if status.lower() == "present":
                    data[name]["Present"] += 1

        print(f"\n{'Name':<20}{'Present':<10}{'Total':<10}{'Percentage':<10}")
        print("-" * 50)
        for name, record in data.items():
            present = record["Present"]
            total = record["Total"]
            percent = (present / total) * 100 if total > 0 else 0
            print(f"{name:<20}{present:<10}{total:<10}{percent:.2f}%")
        print()
    except FileNotFoundError:
        print("No records found. Please add records first.\n")
