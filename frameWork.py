# Generic CRUD Framework

import ast
from Configuration import CONFIGURATION

FILENAME = "details.dat"

STATUS_ACTIVE = "1"
STATUS_DELETED = "0"

records = []
running = True

def print_message(key):
    print(CONFIGURATION["messages"][key].format(domain=CONFIGURATION["domain"]))

def load_records():
    try:
        with open(FILENAME, "r") as fp:
            data = fp.read().strip()
            return ast.literal_eval(data) if data else []
    except (FileNotFoundError, SyntaxError, ValueError):
        return []

def save_records():
    with open(FILENAME, "w") as fp:
        fp.write(str(records))

def show_menu():
    print("\n--- MENU ---")
    for key, value in CONFIGURATION["menu"].items():
        print(f"{key}. {value}")

def get_input(prompt):
    return input(prompt).strip()[:CONFIGURATION["max_field_length"]]

def find_record_index():
    key = get_input(f"Enter {CONFIGURATION['fields'][0]}: ")

    for index, record in enumerate(records):
        if record[0] == key and record[-1] == STATUS_ACTIVE:
            return index
    return -1

def create():
    record = [get_input(f"Enter {field}: ") for field in CONFIGURATION["fields"]]
    record.append(STATUS_ACTIVE)

    records.append(record)
    save_records()
    print_message("created")

def read():
    active_records = [record for record in records if record[-1] == STATUS_ACTIVE]

    if not active_records:
        print_message("no_active")
        return

    print()
    for field in CONFIGURATION["fields"]:
        print(f"{field:<20}", end="")
    print("Status")
    print("-" * (len(CONFIGURATION["fields"]) + 1) * 20)

    for record in active_records:
        for value in record:
            print(f"{value:<20}", end="")
        print()

def update():
    index = find_record_index()
    if index == -1:
        print_message("not_found")
        return

    print("\nUpdatable fields:")
    for i, field in enumerate(CONFIGURATION["fields"][1:], start=2):
        print(f"{i}. {field}")

    try:
        choice = int(input(f"Choose field (2-{len(CONFIGURATION['fields'])}): "))
        if choice < 2 or choice > len(CONFIGURATION["fields"]):
            raise ValueError
    except ValueError:
        print_message("invalid")
        return

    new_value = get_input(f"Enter new {CONFIGURATION['fields'][choice - 1]}: ")

    records[index][choice - 1] = new_value
    save_records()
    print_message("updated")

def delete():
    index = find_record_index()
    if index == -1:
        print_message("not_found")
        return

    records[index][-1] = STATUS_DELETED
    save_records()
    print_message("deleted")

def exit_program():
    global running
    running = False

def main():
    global records
    records = load_records()

    actions = [create, read, update, delete, exit_program]

    while running:
        show_menu()
        try:
            choice = int(input("Enter your choice: "))
            if 1 <= choice <= len(actions):
                actions[choice - 1]()
            else:
                print_message("invalid")
        except ValueError:
            print_message("invalid")

if __name__ == "__main__":
    main()
