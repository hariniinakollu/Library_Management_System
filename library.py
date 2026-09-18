import csv
import os

BOOK_FILE = "books.csv"
MEMBER_FILE = "members.csv"


# Create CSV files if they don't exist
def create_files():
    if not os.path.exists(BOOK_FILE):
        with open(BOOK_FILE, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Book ID", "Title", "Author", "Year", "Status"])

    if not os.path.exists(MEMBER_FILE):
        with open(MEMBER_FILE, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Member ID", "Name", "Phone"])


# Add Book
def add_book():
    book_id = input("Enter Book ID: ")
    title = input("Enter Book Title: ")
    author = input("Enter Author: ")
    year = input("Enter Year: ")

    with open(BOOK_FILE, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([book_id, title, author, year, "Available"])

    print("Book added successfully!")


# View Books
def view_books():
    with open(BOOK_FILE, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)


# Search Book
def search_book():
    key = input("Enter Book ID or Title: ").lower()

    with open(BOOK_FILE, "r") as f:
        reader = csv.DictReader(f)
        found = False

        for row in reader:
            if key in row["Book ID"].lower() or key in row["Title"].lower():
                print(row)
                found = True

        if not found:
            print("Book not found!")


# Update Book
def update_book():
    book_id = input("Enter Book ID to update: ")

    with open(BOOK_FILE, "r") as f:
        rows = list(csv.DictReader(f))

    found = False

    for row in rows:
        if row["Book ID"] == book_id:
            row["Title"] = input("Enter New Title: ")
            row["Author"] = input("Enter New Author: ")
            row["Year"] = input("Enter New Year: ")
            found = True

    with open(BOOK_FILE, "w", newline="") as f:
        fieldnames = ["Book ID", "Title", "Author", "Year", "Status"]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    print("Book updated!" if found else "Book not found!")


# Delete Book
def delete_book():
    book_id = input("Enter Book ID to delete: ")

    with open(BOOK_FILE, "r") as f:
        rows = list(csv.DictReader(f))

    new_rows = [row for row in rows if row["Book ID"] != book_id]

    if len(rows) == len(new_rows):
        print("Book not found!")
        return

    with open(BOOK_FILE, "w", newline="") as f:
        fieldnames = ["Book ID", "Title", "Author", "Year", "Status"]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(new_rows)

    print("Book deleted successfully!")


# Add Member
def add_member():
    member_id = input("Enter Member ID: ")
    name = input("Enter Member Name: ")
    phone = input("Enter Phone Number: ")

    with open(MEMBER_FILE, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([member_id, name, phone])

    print("Member added successfully!")


# View Members
def view_members():
    with open(MEMBER_FILE, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)


# Issue Book
def issue_book():
    book_id = input("Enter Book ID: ")

    with open(BOOK_FILE, "r") as f:
        rows = list(csv.DictReader(f))

    found = False

    for row in rows:
        if row["Book ID"] == book_id:
            found = True

            if row["Status"] == "Available":
                row["Status"] = "Issued"
                print("Book issued successfully!")
            else:
                print("Book is already issued!")

    if not found:
        print("Book not found!")
        return

    with open(BOOK_FILE, "w", newline="") as f:
        fieldnames = ["Book ID", "Title", "Author", "Year", "Status"]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


# Return Book
def return_book():
    book_id = input("Enter Book ID: ")

    with open(BOOK_FILE, "r") as f:
        rows = list(csv.DictReader(f))

    found = False

    for row in rows:
        if row["Book ID"] == book_id:
            found = True

            if row["Status"] == "Issued":
                row["Status"] = "Available"
                print("Book returned successfully!")
            else:
                print("Book is already available!")

    if not found:
        print("Book not found!")
        return

    with open(BOOK_FILE, "w", newline="") as f:
        fieldnames = ["Book ID", "Title", "Author", "Year", "Status"]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


# Main Menu
def main():
    create_files()

    while True:
        print("\n===================================")
        print("      LIBRARY MANAGEMENT SYSTEM")
        print("       USING CSV FILES")
        print("===================================")
        print("1. Add Book")
        print("2. View Books")
        print("3. Search Book")
        print("4. Update Book")
        print("5. Delete Book")
        print("6. Add Member")
        print("7. View Members")
        print("8. Issue Book")
        print("9. Return Book")
        print("10. Exit")
        print("===================================")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_book()

        elif choice == "2":
            view_books()

        elif choice == "3":
            search_book()

        elif choice == "4":
            update_book()

        elif choice == "5":
            delete_book()

        elif choice == "6":
            add_member()

        elif choice == "7":
            view_members()

        elif choice == "8":
            issue_book()

        elif choice == "9":
            return_book()

        elif choice == "10":
            print("Thank you for using Library Management System!")
            break

        else:
            print("Invalid choice!")


main()