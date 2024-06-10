import FoodClass as fc

# this dictionary represents transactions. The key of the dictionary is the transaction identifier.
# The Value of the dictionary is a list. The elements in each list are -
# ['Date', 'Name of item', 'Cost', 'customerid' ]

transactions = {
    'trans1': ['2/15/2023', 'The Lone Patty', 17, 569],
    'trans2': ['2/15/2023', 'The Octobreakfast', 18, 569],
    'trans3': ['2/15/2023', 'The Octoveg', 16, 570],
    'trans4': ['2/15/2023', 'The Octoburger', 20, 570],
}

# Customer data
customers_data = [
    (570, 'Danni Sellyar', '97 Mitchell Way Hewitt Texas 76712', 'dsellyarft@gmpg.org', '254-555-9362', False),
    (569, 'Aubree Himsworth', '1172 Moulton Hill Waco Texas 76710', 'ahimsworthfs@list-manage.com', '254-555-2273', True)
]

def generate_report(customer):
    print("Customer Details")
    print("Customer ID:", customer.get_customerid())
    print("Name:", customer.get_name())
    print("Address:", customer.get_address())
    print("Email:", customer.get_email())
    print("Phone:", customer.get_phone())
    print("Member Status", 'Yes' if customer.get_member_status() else 'No')
    print("\nOrder Details")

    order_total = 0
    for transaction in transactions.values():
        if transaction[3] == customer.get_customerid():
            print(f"Date: {transaction[0]}, Item: {transaction[1]}, Cost: ${transaction[2]:.2f}")
            order_total += transaction[2]

    discount = 0
    if customer.get_member_status():
        discount = order_total * 0.20
        order_total -= discount

    print(f"\nTotal Cost: ${order_total:.2f}")
    if discount > 0:
        print(f"Discount Applied: ${discount:.2f}")

for customer_data in customers_data:
    customer = fc.Customer(*customer_data)
    generate_report(customer)
    print("\n")




