# def credit_card_validator():
#     credit_card = input("Hello, kindly enter your details to verify:  ")
#
#     card_type = get_card_type(credit_card)
#     is_valid = is_credit_card_number_valid(credit_card)
#     calculate_length(credit_card)
#
#     print("Credit Card Type:  ", card_type)
#     if is_valid == credit_card:
#         print("validity status:  ", "valid")
#     else:
#         print("Invalid")
#         is_credit_card_number_valid(credit_card)
#
#
# def get_card_type(credit_card):
#     if credit_card.startswith("4"):
#         return "Visa Card"
#     if credit_card.startswith("5"):
#         return "Master Card"
#     if credit_card.startswith("37"):
#         return "American Express Card"
#     if credit_card.startswith("6"):
#         return "Discover Card"
#     else:
#         return "Invalid card Type"
#
#
# def is_credit_card_number_valid(credit_card):
#         even_total = 0
#         odd_total = 0
#
#         for counter in range(len(credit_card)):
#
#             if counter % 2 == 0:
#                 digit = int(credit_card[counter])
#                 new_digit = digit * 2
#
#                 if new_digit >= 10:
#                     even_total += ((new_digit % 10) + (new_digit // 10))
#                 else:
#                     even_total += new_digit
#
#             if counter % 2 != 0:
#                 digit = int(credit_card[counter])
#                 odd_total += digit
#
#         total_digits = even_total + odd_total
#         if total_digits % 10 == 0:
#             validity_status = "Valid"
#         else:
#             validity_status = "Invalid"
#
#     return validity_status
#     # for num in credit_card[::-1]:
#     #     num = int(num)
#     #     if oddTotal:
#     #         num *= 2
#     #         if num >= 10:
#     #             evenTotal = num % 10 + num / 10
#     #     evenTotal += num
#     #     oddTotal = not oddTotal
#     # return evenTotal % 10 == 0
#
#
# def calculate_length(credit_card):
#     if len(credit_card) <= 16:
#         print("Valid credit card length")
#     else:
#         print("Invalid Credit card length")
#
#
# credit_card_validator()
#
# #             if (counter % 2 == 0){
# #                 int ley = Integer.parseInt(String.valueOf(cardNumber.charAt(counter)));
# #
# #                 if (ley >= 10){
# #                     evenTotal += ley%10+ley/10;
# #                 }
# #                 else
# #                     evenTotal += ley;
# #             }
# #         for (int counter = cardNumber.length()-1; counter >= 0; counter--) {
# #             if (counter % 2 != 0) {
# #                 int ash = Integer.parseInt(String.valueOf(cardNumber.charAt(counter)));
# #
# #                 oddTotal += ash;
# #             }
# #         }
# #        int nda = oddTotal += evenTotal;
# #         if (nda % 10 == 0){
# #             validateStatus = "Valid";
# #         }
# #         else
# #             validateStatus = "Invalid";
# #         return validateStatus;
# #     }
# #
# #
# #
# #
# #
# # if len(creditCard) >= 13 or len(creditCard) <= 16:
# #         print("Invalid Credit card length")
# #     if not re.search('[45637]',)
# #
#
#
# # print("Credit Card Type:  " + creditCard.cardType)
# # print("Credit Card Number:  " + cardNumber)
# # print(len("Credit Card Digit Length:  " + card))
# # print("Credit Card Validity Status:  " + creditCard.validateStatus)
#
# # cardType = "Invalid Card Type"
# # if (len(cardNumber)>= 13) or (len(cardNumber)<= 16):
# #     if not re.search(cardNumber.startsWith("4")):
# #         if cardNumber.startsWith("5"):
# #         if cardNumber.startsWith("37"):
# #     if cardNumber.startsWith("6"):
# #
# #     return cardType;
#
# # cardType = "Visa Card":
# #     cardType = "Master Card":
# #     cardType = "American Express Card":
# #     cardType = "Discover Card":


def collect_card_number():
    collected_card_number = input('Hello, Kindly Enter Card details to verify\n')
    while not collected_card_number.isnumeric():
        print('Invalid card number, card must be digits only')
        collected_card_number = input('Hello, Kindly Enter Card details to verify\n')
    if len(collected_card_number) < 13 or len(collected_card_number) > 16:
        print('Card number length must be between 13 and 16')
        return collect_card_number()
    return collected_card_number


def check_card_type(collected_card_number):
    if collected_card_number.startswith('4'):
        return 'VisaCard'
    elif collected_card_number.startswith('5'):
        return 'MasterCard'
    elif collected_card_number.startswith('6'):
        return 'Discover Cards'
    elif collected_card_number.startswith('37'):
        return 'American Express Card'
    else:
        return 'Invalid Card'


def check_odd_position(collectedCardNumber):
    sum = 0
    for numbers in range(len(card_number) - 2, -1, -2):
        number = int(collectedCardNumber[numbers])
        number = number * 2
        if number > 9:
            number = number - 9
        sum += number
    return sum


def check_even_position(collectedCardNumber):
    sum = 0
    for numbers in range(len(card_number) - 1, -1, -2):
        number = int(collectedCardNumber[numbers])
        sum += number
    return sum


def check_card_validity(collected_card_number):
    odd_position = check_odd_position(collected_card_number)
    even_position = check_even_position(collected_card_number)
    sum = odd_position + even_position
    return 'Valid' if sum % 10 == 0 else 'Invalid'





card_number = collect_card_number()
card_validity = check_card_validity(card_number)
card_type = check_card_type(card_number)



print(f'''
**********************************************************************
**Credit Card Type:  {card_type}
**Credit Card Number:  {card_number}
**Credit Card Digit Length: {len(card_number)}
**Credit Card Validity Status: {card_validity}
**********************************************************************
''')