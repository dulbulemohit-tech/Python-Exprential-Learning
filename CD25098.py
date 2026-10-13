from datetime import datetime, date

birthdays = []

def add_birthday():
    name = input("Enter name: ")
    dob = input("Enter birthday (DD-MM-YYYY): ")

    try:
        datetime.strptime(dob, "%d-%m-%Y")
        birthdays.append([name, dob])
        print("Birthday added successfully!")
    except ValueError:
        print("Invalid date! Use DD-MM-YYYY.")

def view_birthdays():
    if len(birthdays) == 0:
        print("No birthdays saved.")
    else:
        print("\nSaved Birthdays:")
        for person in birthdays:
            print(person[0], "-", person[1])

def search_birthday():
    name = input("Enter name to search: ")

    for person in birthdays:
        if person[0].lower() == name.lower():
            print("Birthday:", person[1])
            return

    print("Birthday not found.")

def delete_birthday():
    name = input("Enter name to delete: ")

    for person in birthdays:
        if person[0].lower() == name.lower():
            birthdays.remove(person)
            print("Birthday deleted successfully!")
            return

    print("Birthday not found.")

def upcoming_birthdays():
    today = date.today()
    found = False

    for person in birthdays:
        dob = datetime.strptime(
            person[1], "%d-%m-%Y"
        ).date()

        next_day = date(today.year, dob.month, dob.day)

        if next_day < today:
            next_day = date(
                today.year + 1, dob.month, dob.day
            )

        days_left = (next_day - today).days

        if days_left <= 30:
            print(person[0], "-", days_left, "days left")
            found = True

    if not found:
        print("No birthdays in the next 30 days.")

while True:
    print("\n===== BIRTHDAY REMINDER =====")
    print("1. Add Birthday")
    print("2. View Birthdays")
    print("3. Search Birthday")
    print("4. Delete Birthday")
    print("5. Upcoming Birthdays")
    print("6. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_birthday()
    elif choice == "2":
        view_birthdays()
    elif choice == "3":
        search_birthday()
    elif choice == "4":
        delete_birthday()
    elif choice == "5":
        upcoming_birthdays()
    elif choice == "6":
        print("Thank you for using Birthday Reminder!")
        break
    else:
        print("Invalid choice! Try again.")
