def main_menu():
    print(f"""WELCOME TO GUARANTY TRUST BANK
        1. Airtime-Self
        2. Airtime-Others
        3. Data
        4. Trsf-GTB
        5. Trsf-Others
        6. Trsf-MFB / eWallet
        7. Quick Transfer
        8. Pay Bills
        9. Next""")
    option = input("Enter your option:  "))
    if option == '1':
        airtime_self()
    elif  option == '2':
        airtime_others()
    elif option == '3':
        Data()
    elif option == '4':
        Trsf_GTB
    elif option == '5':
        Trsf_Others
    elif option == '6':
        Trsf_MFB / eWallet
    elif option == '7':
        Quick Transfer
    elif option == '8':
        Pay Bills
    elif option == '9':
        Next
    else:
        print('Invalid option')
        main_menu()
def airtime_self():
# 7