import random
import customer
import csv
import os

customers = customer.customers
transactions = customer.transactions

# Function to generate a unique transaction ID
def generate_transaction_id():
    while True:
        transaction_id = random.randint(1, 1000)  # You can adjust the range as needed
        if transaction_id not in transactions:
            return transaction_id

def add_transaction():
    customer_id = int(input("Enter customer ID: "))
    if customer_id not in customers:
        print("Customer not found.")
        return

    transaction_id = generate_transaction_id()
    transaction_details = {
        'transaction_id': str(transaction_id),
        'customer_id': customer_id,
        'date': input("Enter transaction date: "),
        'category': input("Enter transaction category: "),
        'value': input("Enter value")
        
    }
    transactions[transaction_id] = transaction_details
    # print(transactions)
    print(f"Transaction added with ID: {transaction_id}")

def search_transactions(search_string):
    search_string = search_string.lower()
    matching_transactions = [(id, data) for id, data in transactions.items() if
                             search_string in str(data).lower()]
    if matching_transactions:
        for id, data in matching_transactions:
            print(f"Transaction ID: {id}, Customer ID: {data['customer_id']}, Date: {data['date']}, Category: {data['category']}, value: {data['value']}")
    else:
        print("No matching transactions found.")

def delete_transaction(transaction_id_to_del):
    transaction_id_to_del = str(transaction_id_to_del)
    matching_transactions = [(id, data) for id, data in transactions.items() if
                             transaction_id_to_del == str(id)]
    if matching_transactions:
        for id, data in matching_transactions:
            transactions.pop(id)
            print("Transaction deleted successfully")
    else:
        print("Transaction Id not found")   

def importcvs(filepath):
    try:
        # Save customer records to a CSV file
        with open(filepath, 'r') as csv_file:
            reader = csv.DictReader(csv_file)
            i=0
            for line in reader:
                i+=1
                if int(line['customer_id']) in customers:
                    transaction_id = generate_transaction_id()
                    transaction_details = {
                        'transaction_id': str(transaction_id),
                        'customer_id': line['customer_id'],
                        'date': line['date'],
                        'category': line['category'],
                        'value': line['value']
                    }
                    transactions[transaction_id] = transaction_details
                else:
                    print(f"Unknown customer ID: {line['customer_id']}")
            print("Import Successful")
            return
    except Exception as e:
        print(e)
        return
def exportcsv(ex_csv_filepath):
    
    if os.path.exists(ex_csv_filepath):
        overwrite_option = input("The file already exists content of the file would be lost. Do you want to overwrite it? (yes/no): ")
        if overwrite_option.lower() != 'yes':
            return
        
    with open(ex_csv_filepath,'w') as csv_file:

        fieldnames = ['transaction_id', 'customer_id', 'date', 'category']
        csv_writer = csv.DictWriter(csv_file,fieldnames,delimiter=',')
        csv_writer.writeheader()
        matching_transaction = [(id,data) for id,data in transactions.items()]
        for id,data in matching_transaction:
            csv_writer.writerow(data)
    print("Transaction records exprot to 'transaction_export.csv'.")
            
