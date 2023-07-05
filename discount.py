price_of_item = int(input("Enter the price of item:  "))
credit_score = int(input("Enter customer credit score:  "))

if credit_score > 50:
    discount = (10/100) * price_of_item
    new_price = price_of_item - discount
    down_payment = new_price * (10/100)
    print("Your credit score is good, you got a 10% discount."
          "\nYour down payment is: ", down_payment)

else:
    down_payment = price_of_item * (25/100)
    print("Your credit score is bad."
          "\nYour down payment", down_payment)


