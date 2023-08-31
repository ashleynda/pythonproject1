import re

import datetime as datetime

storeName = "SEMICOLON STORE"
Branch = "MAIN BRANCH"
Address = "312, HERBERT MACAULY WAY, SABO YABA, LAGOS STATE."
Telephone = "03293828343"
datetime = datetime.datetime.now()

customerName = " "
cashierName = " "
product = []
items_bought = []
items_price = []
items_pieces = []
discount = 0.0
sub_total = 0
customer_bill_total = 0
amountPaid = 0.0


def customer_name():
    entry = str(input("What is the customer's name?  "))
    if re.search("^(?!$)\D+$", entry):
        user_buy()
    else:
        print("Invalid input")
        customer_name()


def user_buy():
    entry = input('What did the user buy?  ')
    if re.search("^(?!$)\D+$", entry):
        pieces()
    else:
        print("Invalid input")
        user_buy()


def pieces():
    quantity = input('How many pieces?  ')
    if quantity.isdigit():
        productNumber.append(int(quantity))
        price_per_unit()
    else:
        print("Invalid input")
        pieces()


def price_per_unit():
    price = input('How much per unit?  ')
    if price.isdigit():
        items_price.append(int(price))
        add_items()
    else:
        print("Invalid input")
        price_per_unit()


def add_items():
    item = input('Add more items?  ' +
                 '\n if yes enter \'Yes\' else enter \'No\' ')

    if re.search("^(?!$)\D+$", item):
        if item.casefold() == "yes":
            user_buy()
        elif item.casefold() == "no":
            cashier_name()
    else:
        print("\nInvalid Entry")
        add_items()


def cashier_name():
    entry = input('What is your name?  ')
    if re.search("^(?!$)\D+$", entry):
        discount()
    else:
        print("Invalid input")
        cashier_name()


def discount():
    discountT = input('How much discount will he get?  ')
    if discountT.isdigit():
        display_invoice()
    else:
        print("Invalid input")
        discount()


def bill_page():
    heading_info()
    double_design()
    header_printer()
    single_design()
    list_printing()
    single_design()
    sub_total_total()
    double_design()
    bill_total()
    double_design()
    print(f"THIS IS NOT A RECEIPT KINDLY PAY {customer_bill_total: .2f}")
    double_design()
    customer_pay()


def header_printer():
    print("\tITEM   ", "\t   QTY   ", "\tPRICE   ", "  \tTOTAL(NGN)  ")


def heading_info():
    global StoreName, Branch, Address, Telephone, cashierName, datetime, customerName
    print(f"\n{StoreName} \n{Branch}  \nLocation: {Address} \nTEL: {Telephone},"
          f"\nDate: {datetime} \nCashier: {cashierName} \nCustomer name: {customerName} ")


def list_printing():
    global sub_total
    for index in range(len(items_bought)):
        total = item_pieces[index] * item_price[index]
        sub_total += total
        print(f"{items_bought[index]: >10}  {item_pieces[index]: >10} {item_price[index]: >10} \t\t {total: >10}")


def restore():
    global sub_total
    sub_total = 0


def sub_total_total():
    print(f"Sub Total: {sub_total: >10.2f} \nDiscount:  {((discount / 100) * sub_total): >10.2f},"
          f"\nVAT @ 17.50%: {((sub_total / 100) * 17.5): >10.2f}")


def bill_total():
    global customer_bill_total

    bill = sub_total - ((discount / 100) * sub_total) + ((sub_total / 100) * 17.5)
    customer_bill_total = bill
    print(f"Bill Total:  {bill: >10.2f}")


def double_design():
    print("=" * 50)


def single_design():
    print("-" * 50)


def customer_pay():
    global amount_paid, customer_bill_total
    try:
        user_input = float(input("How much did the customer give you?"))

        if user_input >= customer_bill_total:
            amount_paid = user_input
        else:
            print("Customer must give you an amount more than or equal to ", customer_bill_total)
            customer_pay()
    except ValueError:
        print("Amount can contain only numbers and decimal point")
        customer_pay()


def amount_customer_paid():
    balance = (amount_paid - customer_bill_total)
    print(f"Amount Paid: {amount_paid: >10.2f} \nBalance: {balance: >10.2f}")


def receipt():
    restore()
    heading_info()
    double_design()
    header_printer()
    single_design()
    list_printing()
    single_design()
    sub_total_total()
    double_design()
    bill_total()
    amount_customer_paid()
    double_design()
    print("\t\t\tTHANK YOU FOR YOUR PATRONAGE")
    double_design()


# customer_name()
# user_buy()
# pieces()
# price_per_unit()
# add_items()
# cashier_name()
# discount()
# display_invoice()
if __name__ == "__main__":
    customerName()
    bill_page()
    receipt()
