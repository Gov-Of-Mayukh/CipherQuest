import csv
import random
from datetime import datetime
import os
s=[]
f=[]
r=[]
a=input('welcome to the complaint request and feedback page...enter c for complaint,r for request and f for feedback..')
if a=='c':
        # File to store complaints
    FILE_NAME = 'complaints.csv'

    # Create file with headers if it doesn't exist
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Ticket_Number', 'Name', 'Email', 'Complaint', 'Date'])

    def generate_ticket_number():
        while True:
            t=random.randint(1,999999)
            if t not in s:
                s.append(t)
                return t
                break
        

    def take_complaint():
        print("=== Complaint Registration System ===")
        name = input("Enter your name: ")
        email = input("Enter your email: ")
        complaint = input("Enter your complaint: ")

        ticket_number = generate_ticket_number()
        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Save to CSV
        with open(FILE_NAME, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([ticket_number, name, email, complaint, date])

        print("\nComplaint submitted successfully!")
        print(f"Your Ticket Number is: {ticket_number}")
        print("Keep it safe for future reference.\n")

    if __name__ == "__main__":
        take_complaint()
elif a=='f':
    # File to store complaints
    FILE_NAME = 'feedback.csv'

    # Create file with headers if it doesn't exist
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Ticket_Number', 'Name', 'Email', 'feedback', 'Date'])

    def generate_ticket_numberf():
        while True:
            ft=random.randint(1,999999)
            if ft not in f:
                f.append(ft)
                return ft
                break
        

    def take_feedback():
        print("=== feedback Registration System ===")
        name = input("Enter your name: ")
        email = input("Enter your email: ")
        complaint = input("Enter your feedback: ")

        ticket_number = generate_ticket_numberf()
        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Save to CSV
        with open(FILE_NAME, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([ticket_number, name, email, complaint, date])

        print("\nfeedback submitted successfully!")
        print(f"Your Ticket Number is: {ticket_number}")
        print("Keep it safe for future reference.\n")

    if __name__ == "__main__":
        take_feedback()
elif a=='r':
            # File to store complaints
    FILE_NAME = 'request.csv'

    # Create file with headers if it doesn't exist
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Ticket_Number', 'Name', 'Email', 'Complaint', 'Date'])

    def generate_ticket_numberr():
        while True:
            t=random.randint(1,999999)
            if rt not in r:
                r.append(rt)
                return rt
                break
        

    def take_request():
        
        print("=== request Registration System ===")
        name = input("Enter your name: ")
        email = input("Enter your email: ")
        complaint = input("Enter your request: ")

        ticket_number = generate_ticket_numberr()
        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Save to CSV
        with open(FILE_NAME, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([ticket_number, name, email, complaint, date])

        print("\nrequest submitted successfully!")
        print(f"Your Ticket Number is: {ticket_number}")
        print("Keep it safe for future reference.\n")

    if __name__ == "__main__":
        take_request()
    

