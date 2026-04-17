import csv

file_path = "data.csv"

def add_record():
    name = input("Enter Student Name: ")
    sid = input("Enter Student ID: ")
    score = int(input("Enter Score: "))

    with open(file_path, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([sid, name, score])

    print("Record added!")

def show_records():
    try:
        with open(file_path, "r") as file:
            reader = csv.reader(file)
            print("\n--- Stored Records ---")
            for row in reader:
                sid, name, score = row
                print(f"ID: {sid} | Name: {name} | Score: {score}")
    except FileNotFoundError:
        print("No file available!")

def analyze_data():
    total_score = 0
    student_count = 0

    try:
        with open(file_path, "r") as file:
            reader = csv.reader(file)
            print("\n--- Performance Analysis ---")

            for row in reader:
                sid, name, score = row
                score = int(score)
                total_score += score
                student_count += 1
                print(f"{name} scored {score}")

        if student_count > 0:
            avg = total_score / student_count
            print(f"\nTotal Score: {total_score}")
            print(f"Average Score: {avg}")
        else:
            print("No records to analyze!")

    except FileNotFoundError:
        print("File not found!")

while True:
    print("\n===== MENU =====")
    print("1. Add Record")
    print("2. Show Records")
    print("3. Analyze Performance")
    print("4. Exit")

    choice = input("Select option: ")

    if choice == "1":
        add_record()
    elif choice == "2":
        show_records()
    elif choice == "3":
        analyze_data()
    elif choice == "4":
        print("Program closed.")
        break
    else:
        print("Enter valid option!")