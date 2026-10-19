
import tracker

print("Welcome to Sleep Log Tracker!")

while True:
    print("\n1. Add Sleep Entry")
    print("2. View Summary")
    print("3. View All Entries")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        tracker.add_entry()

    elif choice == "2":
        tracker.view_summary()

    elif choice == "3":
        tracker.view_all()

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please enter 1-4.")
