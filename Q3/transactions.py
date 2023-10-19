import numpy as np
import random
import customer
import csv
import os


def generate_transaction_id():
    while True:
        transaction_id = random.randint(1, 1000)  # You can adjust the range as needed
        if not np.any(customer.transactions[:, 0] == str(transaction_id)):
            return transaction_id


def add_transaction():
    customer_id = int(input("Enter customer ID: "))
    for row in customer.customers:
        if np.any(row[0] == str(customer_id)):
            transaction_id = generate_transaction_id()
            date = input("Enter transaction date as (DD/MM/YYYY): ")
            category = input("Enter transaction category: ")
            value = input("Enter the sales value: ")

            customer.transactions = np.vstack(
                [
                    customer.transactions,
                    [[transaction_id, customer_id, date, category, value]],
                ]
            )
            print(f"Transaction added with ID: {transaction_id}")
            return
    print("Customer not found")


def search_transactions(search_string):
    for row in customer.transactions:
        if np.any(row == str(search_string)):
            print(
                f"Transaction ID: {row[0]}, Customer ID: {row[1]}, Date: {row[2]}, Category: {row[3]}, Sales_value: {row[4]}"
            )
            return


def delete_transaction(transaction_id_to_del):
    i = 0
    for row in customer.transactions:
        if np.any(row[0] == str(transaction_id_to_del)):
            customer.transactions = np.delete(customer.transactions, i, axis=0)
            print("Customer and associated transactions deleted successfully.")
            return
        i += 1
    print("No matching transaction found.")


def importcsv(csv_filepath):
    try:
        with open(csv_filepath, "r") as f:
            reader = csv.reader(f)
            next(reader)
            for data in reader:
                if np.any(customer.customers[:,0] == str(data[0])):
                    transaction_id = generate_transaction_id()
                    customer_id = data[0]
                    date = data[1]
                    category = data[2]
                    value = data[3]

                    customer.transactions = np.vstack(
                        [
                            customer.transactions,
                            [[transaction_id, customer_id, date, category, value]],
                        ]
                    )
        print("Import Successful")
    except Exception as e:
        print(e)
        return


def exportcsv(ex_csv_filepath):

    if os.path.exists(ex_csv_filepath):
        overwrite_option = input("The file already exists content of the file would be lost. Do you want to overwrite it? (yes/no): ")
        if overwrite_option.lower() != 'yes':
            return

    header = np.array(
        [["Transaction_id", "Customer_id", "Date", "Category", "Sales_value"]]
    )
    data_with_header = np.vstack((header, customer.transactions))
    try:
        with open(ex_csv_filepath, "w", newline="") as o:
            csvwriter = csv.writer(o, delimiter=",")
            for row in data_with_header:
                csvwriter.writerow(row)
            print("Export Successful")
    except Exception as e:
        print(e)
        return
