import matplotlib.pyplot as plt
import numpy as np
import customer
from datetime import datetime


sales_value_array = np.array([], dtype=object).reshape(0, 3)
c_id_in_postalcode = np.array([],dtype=object)

def empty_array():
    global sales_value_array
    sales_value_array = np.empty_like(sales_value_array)

def transaction_numbers():
    empty_array()
    global sales_value_array
    month_id = 1
    for row1 in customer.transactions:
        count = 0
        sales_value = 0

        if month_id >= 13:
            plt.plot(
                sales_value_array[:, 1],
                sales_value_array[:, 2],
                label="The monthly sales values and transaction numbers",
                marker="o",
            )
            plt.xlabel("Transaction Numbers")
            plt.ylabel("Monthly Sales Value")
            plt.legend()
            plt.show()
            return

        for row2 in customer.transactions:
            date = row2[2]
            date_object = datetime.strptime(date, "%m/%d/%Y")
            month = date_object.month

            if month_id == month:
                sales_value += int(row2[4])
                count += 1

        data = np.array([month_id, count, sales_value])
        sales_value_array = np.vstack([sales_value_array, data])

        month_id += 1


def transaction_numbers_given_customer(customer_id):
    empty_array()
    global sales_value_array
    month_id = 1
    
    for row1 in customer.transactions:
        count = 0
        sales_value = 0

        if month_id >= 13:
            plt.plot(
                sales_value_array[:, 1],
                sales_value_array[:, 2],
                label="The monthly sales values and transaction numbers",
                marker="o",
            )
            plt.xlabel("Transaction Numbers")
            plt.ylabel("Monthly Sales Value")
            plt.legend()
            plt.show()
            return

        for row2 in customer.transactions:
            if row2[1] == str(customer_id):
                date = row2[2]
                date_object = datetime.strptime(date, "%m/%d/%Y")
                month = date_object.month

                if month_id == month:
                    sales_value += int(row2[4])
                    count += 1

        data = np.array([month_id, count, sales_value])
        sales_value_array = np.vstack([sales_value_array, data])

        month_id += 1

def transaction_numbers_given_postcode(postcode):
    empty_array()
    global sales_value_array
    global c_id_in_postalcode

    for row in customer.customers:
        if np.any(row[2] == str(postcode)):
            c_id = row[0]
            c_id_in_postalcode = np.append(c_id_in_postalcode,c_id)
    
    month_id = 1
    
    for row1 in customer.transactions:
        count = 0
        sales_value = 0

        if month_id >= 13:
            plt.plot(
                sales_value_array[:, 1],
                sales_value_array[:, 2],
                label="The monthly sales values and transaction numbers",
                marker="o",
            )
            plt.xlabel("Transaction Numbers")
            plt.ylabel("Monthly Sales Value")
            plt.legend()
            plt.show()
            return

        for row2 in customer.transactions:
            if row2[1] == np.any(c_id_in_postalcode):
                date = row2[2]
                date_object = datetime.strptime(date, "%m/%d/%Y")
                month = date_object.month

                if month_id == month:
                    sales_value += int(row2[4])
                    count += 1

        data = np.array([month_id, count, sales_value])
       
        sales_value_array = np.vstack([sales_value_array, data])

        month_id += 1
    
