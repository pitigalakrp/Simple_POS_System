import random
import csv
import os

customers = {}
transactions = {}

# Function to generate a unique customer ID
def generate_customer_id():
    while True:
        customer_id = random.randint(1, 10)  # You can adjust the range as needed
        if customer_id not in customers:
            return customer_id

# Function to add a new customer
def add_customer():
    customer_name = input("Enter customer's name: ")
    customer_id = generate_customer_id()
    customer_details = {
        'customer_id':str(customer_id),
        'name': customer_name,
        'postcode': input("Enter customer's postcode (optional): "),
        'phone_number': input("Enter customer's phone number (optional): ")
    }
    customers[customer_id] = customer_details
    print(f"Customer added with ID: {customer_id}")

def search_customers(search_string):
    search_string = search_string.lower()
    matching_customers = [(id, data) for id, data in customers.items() if
                          search_string in str(data).lower()]
    if matching_customers:
        for id, data in matching_customers:
            print(f"Customer ID: {id}, Name: {data['name']}")
    else:
        print("No matching customers found.")

def display_transactions_for_customer(customer_id):
    customer_id = str(customer_id)
    matching_transactions = [(id, data) for id, data in transactions.items() if
                             customer_id == str(data['customer_id'])]
    if matching_transactions:
        for id, data in matching_transactions:
            print(f"Transaction ID: {id}, Customer ID: {data['customer_id']}, Date: {data['date']}, Category: {data['category']}")
    else:
        print("No transactions found for this customer.")


# Function to delete a customer with a given customer ID and associated transactions
def delete_customer(customer_id_to_del):
    customer_id_to_del = str(customer_id_to_del)
    matching_customer = [(id, data) for id, data in customers.items() if
                             customer_id_to_del == str(id)]
    if matching_customer:
        for id, data in matching_customer:
            customers.pop(id)
            #   Delete associated transactions
            transactions_to_delete = [id for id, data in transactions.items() if
                                   str(customer_id_to_del) == str(data['customer_id'])]
            for id in transactions_to_delete:
                del transactions[id]
                print("Customer and associated transactions deleted successfully.")
    else:
        print("Customer not found.")

def importcvs(filepath):
    # Import customer records to a CSV file
    try:    
        with open(filepath, 'r') as csv_file:
            reader = csv.DictReader(csv_file)
            for line in reader:
                if int(line['customer_id']) not in customers:
                    customers[int(line['customer_id'])] = line
                    print(f"Customer added with ID: {line['customer_id']}")
                else:
                    print(f"ID: {line['customer_id']} Already Exists")
    except Exception as e:
        print(e)
        return
           
def exportcsv(ex_csv_filepath):

    if os.path.exists(ex_csv_filepath):
        overwrite_option = input("The file already exists content of the file would be lost. Do you want to overwrite it? (yes/no): ")
        if overwrite_option.lower() != 'yes':
            return
    with open(ex_csv_filepath,'w') as csv_file:

        fieldnames = ['customer_id', 'name', 'postcode', 'phone_number']
        csv_writer = csv.DictWriter(csv_file,fieldnames,delimiter=',')
        csv_writer.writeheader()
        matching_customers = [(id,data) for id,data in customers.items()]
        for id,data in matching_customers:
            csv_writer.writerow(data)
            

    print(f"Customer records exprot to {ex_csv_filepath}.")

