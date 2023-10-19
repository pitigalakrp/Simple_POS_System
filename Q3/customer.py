import numpy as np
import random
import csv
import os

customers = np.array([], dtype=str).reshape(0, 4)
transactions = np.array([], dtype=str).reshape(0, 5)


# Function to generate a unique customer ID
def generate_customer_id():
    while True:
        global customers
        customer_id = random.randint(1, 10)  # You can adjust the range as needed
        if not np.any(customers[:, 0] == str(customer_id)):
            return customer_id


def add_customer():
    global customers
    customer_name = input("Enter customer's name: ")
    customer_id = generate_customer_id()
    postcode = input("Enter customer's postcode (optional): ")
    phone_number = input("Enter customer's phone number (optional): ")

    customers = np.vstack(
        [customers, [[customer_id, customer_name, postcode, phone_number]]]
    )
    print(f"Customer add with ID: {customer_id}")


def search_customers(search_string):
    global customers
    for row in customers:
        if np.any(row == str(search_string)):
            print(f"Customer ID: {row[0]}, Name: {row[1]}")
            return

    print("No matching customers found.")


def display_transactions_for_customer(customer_id):
    global transactions
    for row in transactions:
        if np.any(row[1] == str(customer_id)):
            print(
                f"Transaction ID: {row[0]}, Customer ID: {row[1]}, Date: {row[2]}, Category: {row[3]}, Sales_value: {row[4]}"
            )
            return


def delete_customer(customer_id_to_del):
    global customers
    global transactions
    i = 0
    j = 0

    if not np.any(customers[:, 0] == customer_id_to_del):
        print("No matching customers found.")
        return

    for row in customers:
        if np.any(row[0] == str(customer_id_to_del)):
            customers = np.delete(customers, i, axis=0)
            break
        else:
            i += 1

    for row in transactions:
        if np.any(row[1] == str(customer_id_to_del)):
            transactions = np.delete(transactions, j, axis=0)
        else:
            if j < len(transactions):
                j += 1
    print("Customer and associated transactions deleted successfully.")


def importcsv(csv_filepath):
    global customers
    try:
       
        with open(csv_filepath, "r") as f:
            reader = csv.reader(f)
            next(reader)
            for data in reader:
                customers = np.vstack([customers, data])
            print("Import Successful")
    except Exception as e:
        print(e)
        return


def exportcsv(ex_csv_filepath):
    global customers
    if os.path.exists(ex_csv_filepath):
        overwrite_option = input("The file already exists content of the file would be lost. Do you want to overwrite it? (yes/no): ")
        if overwrite_option.lower() != 'yes':
            return
    header = np.array([["customer_id", "name", "postcode", "phone"]])
    data_with_header = np.vstack((header, customers))
    try:
        with open(ex_csv_filepath, "w", newline="") as o:
            csvwriter = csv.writer(o, delimiter=",")
            for row in data_with_header:
                csvwriter.writerow(row)
            print("Export Successful")
    except Exception as e:
        print(e)
        return
