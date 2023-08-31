def your_vat():
    while True:
        try:
            price_of_item = int(input('Enter the price if an item:  '))
            vat = float(input('Enter the vat:  '))

            if price_of_item < 0 or vat < 0:
                print("Numbers entered must be positive")
            else:
                vat_total = price_of_item * (vat / 100)
                final_price_vat = price_of_item + vat_total
                return final_price_vat
        except ValueError:
            print("Invalid input")


print(your_vat())
