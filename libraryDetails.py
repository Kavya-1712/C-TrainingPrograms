FILENAME = "library.txt"

def get_field_names():
    return ["Book ID", "Book Name", "Quantity", "Active"]

def load_records_from_file():
    records = []
    try:
        with open(FILENAME, "r") as fpLibrary:
            for record in fpLibrary:
                records.append(record.strip().split())
    except FileNotFoundError:
        pass
    return records

def save_records_to_file(records):
    with open(FILENAME, "w") as fpLibrary:
        for record in records:
            fpLibrary.write(" ".join(record) + "\n")

def find_record_index(book_id, records):
    for index, record in enumerate(records):
        if record[0] == book_id and record[3] == "1":
            return index
    return -1

def show_menu():
    print("1. Add Book\n2. Display Books\n3. Update Book Quantity\n4. Delete Book\n5. Exit\n")
    choice = input("Enter your choice: ")
    if not choice.isdigit():
        return -1
    return int(choice)

def get_active_book():
    records = load_records_from_file()
    book_id = input("Enter Book ID: ")

    index = find_record_index(book_id, records)
    if index == -1:
        print("Book not found or already deleted.\n")
        return None, None

    return records, index


def add_book():
    records = load_records_from_file()

    book_id = input("Enter Book ID: ")
    book_name = input("Enter Book Name (use _ instead of space): ")
    quantity = input("Enter Quantity: ")

    records.append([book_id, book_name, quantity, "1"])
    save_records_to_file(records)

    print("Book added successfully.\n")

def display_books():
    records = load_records_from_file()
    fields = get_field_names()

    active_records = [record for record in records if record[3] == "1"] 

    if not active_records:
        print("Library is empty.\n")
        return

    for record in active_records:
        for i in range(len(fields) - 1):
            print(f"{fields[i]}: {record[i]}")
        print()

def update_book_quantity():
    records, index = get_active_book()
    if records is None:
        return

    new_quantity = input("Enter new quantity: ")
    records[index][2] = new_quantity

    save_records_to_file(records)
    print("Quantity updated successfully.\n")

def delete_book():
    records, index = get_active_book()
    if records is None:
        return

    records[index][3] = "0"
    save_records_to_file(records)

    print("Book deleted successfully.\n")

def exit_program():
    print("Exiting program.")
    raise SystemExit

def main():
    options = [add_book, display_books, update_book_quantity, delete_book, exit_program]

    while True:
        choice = show_menu()

        if 1 <= choice <= 5:
            options[choice - 1]()
        else:
            print("Invalid choice.\n")

if __name__ == "__main__":
    main()
