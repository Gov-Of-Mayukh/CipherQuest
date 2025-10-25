# view_records.py
import csv

def view_records(filename):
    try:
        with open(filename, "r") as file:
            reader = csv.reader(file)
            print(f"\n{'Name':<20}{'Date':<15}{'Status':<10}")
            print("-" * 45)
            for row in reader:
                if len(row) == 3:
                    print(f"{row[0]:<20}{row[1]:<15}{row[2]:<10}")
        print()
    except FileNotFoundError:
        print("No records found. Please add records first.\n")
