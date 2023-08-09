def credit_card_validator():
    credit_card = input("Hello, kindly enter your details to verify:  ")

    card_type = get_card_type(credit_card)
    # is_valid = is_credit_card_number_valid(credit_card)
    calculate_length(credit_card)

    print("Credit Card Type:  ", card_type)
    if is_valid == credit_card:
        print("validity status:  ", "valid")
    else:
        print("Invalid")
        is_credit_card_number_valid(credit_card)


def get_card_type(credit_card):
    if credit_card.startswith("4"):
        return "Visa Card"
    if credit_card.startswith("5"):
        return "Master Card"
    if credit_card.startswith("37"):
        return "American Express Card"
    if credit_card.startswith("6"):
        return "Discover Card"
    else:
        return "Invalid card Type"


def is_credit_card_number_valid(credit_card):
    evenTotal = 0
    oddTotal = 0
    for num in credit_card[::-1]:
        num = int(num)
        if oddTotal:
            num *= 2
            if num >= 10:
                evenTotal = num % 10 + num / 10
        evenTotal += num
        oddTotal = not oddTotal
    return evenTotal % 10 == 0


def calculate_length(credit_card):
    if len(credit_card) <= 16:
        print("Valid credit card length")
    else:
        print("Invalid Credit card length")


credit_card_validator()

#             if (counter % 2 == 0){
#                 int ley = Integer.parseInt(String.valueOf(cardNumber.charAt(counter)));
#
#                 if (ley >= 10){
#                     evenTotal += ley%10+ley/10;
#                 }
#                 else
#                     evenTotal += ley;
#             }
#         for (int counter = cardNumber.length()-1; counter >= 0; counter--) {
#             if (counter % 2 != 0) {
#                 int ash = Integer.parseInt(String.valueOf(cardNumber.charAt(counter)));
#
#                 oddTotal += ash;
#             }
#         }
#        int nda = oddTotal += evenTotal;
#         if (nda % 10 == 0){
#             validateStatus = "Valid";
#         }
#         else
#             validateStatus = "Invalid";
#         return validateStatus;
#     }
#
#
#
#
#
# if len(creditCard) >= 13 or len(creditCard) <= 16:
#         print("Invalid Credit card length")
#     if not re.search('[45637]',)
#


# print("Credit Card Type:  " + creditCard.cardType)
# print("Credit Card Number:  " + cardNumber)
# print(len("Credit Card Digit Length:  " + card))
# print("Credit Card Validity Status:  " + creditCard.validateStatus)

# cardType = "Invalid Card Type"
# if (len(cardNumber)>= 13) or (len(cardNumber)<= 16):
#     if not re.search(cardNumber.startsWith("4")):
#         if cardNumber.startsWith("5"):
#         if cardNumber.startsWith("37"):
#     if cardNumber.startsWith("6"):
#
#     return cardType;

# cardType = "Visa Card":
#     cardType = "Master Card":
#     cardType = "American Express Card":
#     cardType = "Discover Card":
