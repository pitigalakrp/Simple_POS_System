import random
import csv
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

