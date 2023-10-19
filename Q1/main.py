import transactions
import customer
import csv
# Main menu loop

while True:
    print("\nWESTERN WHOLESALE PVT LTD")
    print("")
    print("\nMain Menu:")
    print("")
    print("1. Add a new customer")
    print("2. Add a new transaction")
    print("3. Search customers")
    print("4. Search sales transactions")
    print("5. Display sales transactions for a given customer")
    print("6. Delete a transaction record")
    print("7. Delete a customer with associated transactions")
    print("8. Quit")
    choice = input("Enter your choice (1-8): ")
    
    if choice == '1':
        customer.add_customer()
    elif choice == '2':
        transactions.add_transaction()
    elif choice == '3':
        search_string = input("Enter search string: ")
        customer.search_customers(search_string)
    elif choice == '4':
        search_string = input("Enter search string: ")
        transactions.search_transactions(search_string)
    elif choice == '5':
        customer_id = input("Enter customer ID: ")
        customer.display_transactions_for_customer(customer_id)
    elif choice == '6':
        transaction_id_to_del = input("Enter transaction ID: ")
        transactions.delete_transaction(transaction_id_to_del)
    elif choice == '7':
        customer_id_to_del = input("Enter customer ID: ")
        customer.delete_customer(customer_id_to_del)
    elif choice == '8':
        break
    else:
        print("Invalid choice. Please choose a valid option (1-8).")
print("Goodbye!")

