def chat():
    pass


def main_menu():
    print(f""" List of menu functions
         1. Phone book
         2. Messages
         3. Chat
         4. Call register
         5. Tones
         6. Settings
         7. Call divert
         8. Games
         9. Calculator
         10. Reminders
         11. Clock
         12. Profiles
         13. SIM services""")
    option = int(input("Enter your option:  "))
    if option == 1:
        phonebook()
    elif option == 2:
        messages()
    elif option == 3:
        chat()


def back_menu():
    print('0. for back to menu')
    option1 = int(input("Enter your option:  "))
    if option1 == 0:
        main_menu()


def phonebook():
    print(f"""
            1. Search
            2. Service No.s
            3. Add name
            4. Erase
            5. Edit
            6. Assign tone
            7. Send b'card
            8. Options 
            9. Speed dials
            10. Voice tags
            0. Back""")
    option = int(input("Enter your option:  "))
    if option == 0:
        main_menu()


# def back():
#     print('0. for back to menu')
#     option = int(input("Enter your option:  "))
#         if option == 8:
#             print(f"""
#          1. Type of view
#          2. Memory status """)
#     option = int(input("Enter your option:  "))


def messages():
    print(f"""
     1. Write messages
     2. Inbox
     3. Outbox
     4. Picture messages
     5. Templates
     6. Smileys
     7. Message settings 
     8. Info service
     9. Voice mailbox number
     10. Service command editor""")
    option = int(input("Enter your option:  "))
    if option == 7:
        print(f"""
     1. Set 1
     2. Common 
     """)


#     option = int(input("Enter your option:  "))
#     if option == 1:
#         print(f"""
#      1. Message centre number
#      2. Messages sent as
#      3. Messages validity """)
#     if option == 2:
#         print(f"""
#      1. Delivery reports
#      2. Reply via same centre
#      3. Character support """)
# elif option == 3:
#     print("Chat")
#     option = int(input("Enter your option:  "))
# elif option == 4:
#     print(f"""
#      1. Missed calls
#      2. Received calls
#      3. Dialled numbers
#      4. Erase recent call lists
#      5. Show call duration
#      6. Show call costs
#      7. Call cost settings
#      8. Prepaid credit """)
#     option = int(input("Enter your option:  "))
#     if option == 5:
#         print(f"""
#      1. Last call duration
#      2. All calls' duration
#      3. Received calls' duration
#      4. Dialled calls' duration
#      5. Clear timers """)
#     if option == 6:
#         print(f"""
#         1. Last call cost
#         2. All calls' cost
#         3. Clear counters
#         """)
#     if option == 7:
#         print(f"""
#         1.Call cost limit
#         2. Show costs in
#         """)
# elif option == 5:
#     print(f"""
#      1. Ringing tone
#      2. Ringing volume
#      3. Incoming call alert
#      4. Composer
#      5. Message alert tone
#      6. Keypad tones
#      7. Warning and game tone
#      8. Vibrating alert
#      9. Screen saver """)
#     option = int(input("Enter your option:  "))
# elif option == 6:
#     print(f"""
#      1. Call settings
#      2. Phone settings
#      3. Security settings
#      4. Restore factory settings""")
#     option = int(input("Enter your option:  "))
#     if option == 1:
#         print(f"""
#      1. Automatic redial
#      2. Speed dialling
#      3. Call waiting options
#      4. Own number sending
#      5. Phone line in use
#      6. Automatic answer """)
#     if option == 2:
#         print(f"""
#      1. Language
#      2. Cell info display
#      3. Welcome note
#      4. Network selection
#      5. Lights
#      6. Confirm SIM service actions """)
#     if option == 3:
#         print("""
#      1. PIN code request
#      2. Call barring service
#      3. Fixed dialling
#      4. Closed user group
#      5. Phone security
#      6. Change acce """)
# elif option == 7:
#     print("Call divert")
#     option = int(input("Enter your option:  "))
# elif option == 8:
#     print("Games")
#     option = int(input("Enter your option:  "))
# elif option == 9:
#     print("Calculator")
#     option = int(input("Enter your option:  "))
# elif option == 10:
#     print("Reminders")
#     option = int(input("Enter your option:  "))
# elif option == 11:
#     print(f"""
#      1. Alarm clock
#      2. Clock settings
#      3. Date setting
#      4. Stopwatch
#      5. Countdown timer
#      6. Auto update of date and time""")
#     option = int(input("Enter your option:  "))
# elif option == 12:
#     print("Profiles")
#     option = int(input("Enter your option:  "))
# elif option == 13:
#     print("SIM services")
# option = int(input("Enter your option:  "))
# print()
# option = int(input("Enter your option:  "))


main_menu()
