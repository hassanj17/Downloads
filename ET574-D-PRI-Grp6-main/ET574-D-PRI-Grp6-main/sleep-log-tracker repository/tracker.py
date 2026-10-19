import datetime
import data


# Add a new sleep entry
def add_entry():
    # Get and validate the date
    while True:
        date = input("Enter date (YYYY-MM-DD): ").strip()

        try:
            datetime.datetime.strptime(date, "%Y-%m-%d")

            if date in data.dates:
                print("An entry for this date already exists.")
                continue

            break

        except ValueError:
            print("Invalid date. Please use YYYY-MM-DD.")

    # Get and validate hours slept
    while True:
        try:
            hours = float(input("Enter hours slept (0-24): "))

            if 0 <= hours <= 24:
                break

            print("Enter a number from 0 to 24.")

        except ValueError:
            print("Please enter a valid number.")

    # Get and validate sleep quality
    while True:
        try:
            quality = int(input("Enter sleep quality (1-5): "))

            if 1 <= quality <= 5:
                break

            print("Sleep quality must be from 1 to 5.")

        except ValueError:
            print("Please enter a whole number.")

    # Get optional notes
    note = input("Enter notes (optional): ").strip()

    # Save the entry
    data.dates.append(date)
    data.hours_slept.append(hours)
    data.sleep_quality.append(quality)
    data.notes.append(note)

    print("Sleep entry added successfully!")


# Print every sleep entry using the parallel lists
def view_all():
    # If there are no entries, tell the user and exit
    if len(data.dates) == 0:
        print("\nNo sleep entries yet.")
        return

    print("\n--- All Sleep Entries ---")
    for i in range(len(data.dates)):
        print(f"Entry {i + 1}")
        print(f"  Date:    {data.dates[i]}")
        print(f"  Hours:   {data.hours_slept[i]}")
        print(f"  Quality: {data.sleep_quality[i]}/5")
        if data.notes[i] != "":
            print(f"  Notes:   {data.notes[i]}")
        else:
            print("  Notes:   (none)")
        print()


# Show total entries, total/average hours, and best/worst sleep quality
def view_summary():
    # If there are no entries, tell the user and exit
    if len(data.dates) == 0:
        print("\nNo sleep entries yet.")
        return

    total_entries = len(data.dates)
    total_hours = sum(data.hours_slept)
    average_hours = total_hours / total_entries

    best_quality = max(data.sleep_quality)
    worst_quality = min(data.sleep_quality)

    # Find the matching dates using the parallel lists
    best_index = data.sleep_quality.index(best_quality)
    worst_index = data.sleep_quality.index(worst_quality)

    print("\n--- Sleep Summary ---")
    print(f"Total entries:   {total_entries}")
    print(f"Total hours:     {total_hours:.1f}")
    print(f"Average hours:   {average_hours:.2f}")
    print(f"Best quality:    {best_quality}/5 (on {data.dates[best_index]})")
    print(f"Worst quality:   {worst_quality}/5 (on {data.dates[worst_index]})")
