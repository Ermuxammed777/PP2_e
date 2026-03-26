import psycopg2
import csv

conn = psycopg2.connect(
    dbname="phonebook",
    user="ermuhammed",
    host="localhost",
    port="5432"
)

cur = conn.cursor()

# создать таблицу
cur.execute("""
CREATE TABLE IF NOT EXISTS contacts (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    phone VARCHAR(20)
);
""")
conn.commit()


# 1. INSERT from console
def insert_from_console():
    name = input("Enter name: ")
    phone = input("Enter phone: ")

    cur.execute("INSERT INTO contacts (name, phone) VALUES (%s, %s)", (name, phone))
    conn.commit()
    print("Contact added!")


# 2. INSERT from CSV
def insert_from_csv():
    filename = input("Enter CSV filename: ")

    with open(filename, newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            name, phone = row
            cur.execute("INSERT INTO contacts (name, phone) VALUES (%s, %s)", (name, phone))

    conn.commit()
    print("CSV data inserted!")


# 3. UPDATE
def update_contact():
    name = input("Enter name to update: ")
    new_name = input("New name (or press Enter to skip): ")
    new_phone = input("New phone (or press Enter to skip): ")

    if new_name:
        cur.execute("UPDATE contacts SET name=%s WHERE name=%s", (new_name, name))
    if new_phone:
        cur.execute("UPDATE contacts SET phone=%s WHERE name=%s", (new_phone, name))

    conn.commit()
    print("Updated!")


# 4. QUERY with filters
def query_contacts():
    print("1. Show all")
    print("2. Search by name")
    print("3. Search by phone prefix")

    choice = input("Choose: ")

    if choice == "1":
        cur.execute("SELECT * FROM contacts")

    elif choice == "2":
        name = input("Enter name: ")
        cur.execute("SELECT * FROM contacts WHERE name ILIKE %s", ('%' + name + '%',))

    elif choice == "3":
        prefix = input("Enter phone prefix: ")
        cur.execute("SELECT * FROM contacts WHERE phone LIKE %s", (prefix + '%',))

    rows = cur.fetchall()
    for row in rows:
        print(row)


# 5. DELETE
def delete_contact():
    print("1. Delete by name")
    print("2. Delete by phone")

    choice = input("Choose: ")

    if choice == "1":
        name = input("Enter name: ")
        cur.execute("DELETE FROM contacts WHERE name=%s", (name,))
    elif choice == "2":
        phone = input("Enter phone: ")
        cur.execute("DELETE FROM contacts WHERE phone=%s", (phone,))

    conn.commit()
    print("Deleted!")


# MENU
while True:
    print("\n--- PHONEBOOK ---")
    print("1. Insert from console")
    print("2. Insert from CSV")
    print("3. Update contact")
    print("4. Query contacts")
    print("5. Delete contact")
    print("0. Exit")

    choice = input("Choose option: ")

    if choice == "1":
        insert_from_console()
    elif choice == "2":
        insert_from_csv()
    elif choice == "3":
        update_contact()
    elif choice == "4":
        query_contacts()
    elif choice == "5":
        delete_contact()
    elif choice == "0":
        break
    else:
        print("Invalid choice!")

cur.close()
conn.close()