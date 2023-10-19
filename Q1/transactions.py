import random
import customer

customers = customer.customers
transactions = customer.transactions

# Function to generate a unique transaction ID
def generate_transaction_id():
    while True:
        transaction_id = random.randint(1, 10)  # You can adjust the range as needed
        if transaction_id not in transactions:
            return transaction_id

def add_transaction():
    customer_id = int(input("Enter customer ID: "))
    if customer_id not in customers:
        print("Customer not found.")
        return

    transaction_id = generate_transaction_id()
    transaction_details = {
        'customer_id': customer_id,
        'date': input("Enter transaction date: "),
        'category': input("Enter transaction category: ")
        
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
            print(f"Transaction ID: {id}, Customer ID: {data['customer_id']}, Date: {data['date']}, Category: {data['category']}")
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
            
