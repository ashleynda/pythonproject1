def main_menu():
    print(f"""
        1. Phone book
        2. Messages
        3. Chat
        4.Call register
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
    elif option == 4:
        call_register()
    elif option == 5:
        tones()
    elif option == 6:
        settings()
    elif option == 7:
        call_divert()
    elif option == 8:
        games()
    elif option == 9:
        calculator()
    elif option == 10:
        reminders()
    elif option == 11:
        clock()
    elif option == 12:
        profiles()
    elif option == 13:
        sim_services()
    else:
        print('invalid option')
        main_menu()


# def back_menu1():
#   print('00. main menu')
#  print('0. previous')
# option1 = int(input("Enter your option:  "))
# if option == 00:
#   main_menu()
# if option == 0:
#   back_menu1()


def options():
    print(f"""
            1. Type of view
            2. Memory status
            3. Previous
            4. Main menu""")
    option = int(input("Enter your option:  "))
    if option == 4:
        main_menu()
    elif option == 3:
        phonebook()
    else:
        print('Invalid option')
        options()


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
        11. main menu""")
    option = int(input("Enter your option:  "))
    if option == 11:
        main_menu()
    elif option == 8:
        options()


def set_():
    print(f"""
           1. Message centre number
           2. Messages sent as 
           3. Messages validity
           4. Previous
           5. Back to messages
           6. Main menu""")
    option = int(input("Enter your option:  "))
    if option == 4:
        message_settings()
    elif option == 5:
        messages()
    elif option == 6:
        main_menu()
    else:
        print('Invalid option')
        message_settings()


def common():
    print(f"""
            1. Delivery reports
            2. Reply via same centre
            3. Character support
            4. Previous
            5. Back to messages
            6. Main menu""")
    option = int(input("Enter your option:  "))
    if option == 4:
        message_settings()
    elif option == 5:
        messages()
    elif option == 6:
        main_menu()
    else:
        print('Invalid option')
        message_settings()


def message_settings():
    print(f"""
            1. Set 
            2. Common 
            3. previous
            4. main menu""")
    option = int(input("Enter your option:  "))
    if option == 4:
        main_menu()
    elif option == 1:
        set_()
    elif option == 2:
        common()
    elif option == 3:
        messages()
    else:
        print('Invalid option')
        message_settings()


def messages():
    print(f"""
        1. Write message
        2. Inbox
        3. Outbox
        4. Picture message
        5. Templates
        6. Smileys
        7. Message settings
        8. Info service
        9. Voice mailbox number
        10. Service command editor
        11. main menu""")
    option = int(input("Enter your option:  "))
    if option == 11:
        main_menu()
    if option == 7:
        message_settings()
    if option == 1:
        set_()
        option = int(input("Enter your option:  "))
    if option == 2:
        common()
        option = int(input("Enter your option:  "))


def chat():
    print(f"""
        Chat
        1. Back to menu""")
    option = int(input("Enter your option:  "))
    if option == 1:
        main_menu()


def show_call_duration():
    print(f"""
            1. Last call duration
            2. All calls' duration
            3. Received calls' duration
            4. Dialled calls' duration
            5. Clear timers
            6. Back to call register
            7. main menu""")
    option = int(input("Enter your option:  "))
    if option == 6:
        call_register()
    elif option == 7:
        main_menu()
    else:
        print('Invalid option')
        show_call_duration()


def show_call_costs():
    print(f"""
            1. Last call cost
            2. All calls' cost
            3. Clear counters
            4. Back to call register
            5.. main menu""")
    option = int(input("Enter your option:  "))
    if option == 5:
        main_menu()
    elif option == 4:
        call_register()

    else:
        print('Invalid option')
        show_call_costs()


def call_cost_settings():
    print(f"""
            1.Call cost limit
            2. Show costs in
            3. Back to call register
            4. main menu""")
    option = int(input("Enter your option:  "))
    if option == 3:
        call_register()
    elif option == 4:
        main_menu()
    else:
        print('Invalid option')
        message_settings()


def call_register():
    print(f"""
        1. Missed calls
        2. Received calls
        3. Dialled numbers1
        4. Erase recent call lists
        5. Show call duration
        6. Show call costs
        7. Call cost settings
        8. Prepaid credit
        9. main menu""")
    option = int(input("Enter your option:  "))
    if option == 5:
        show_call_duration()
    if option == 6:
        show_call_costs()
    if option == 7:
        call_cost_settings()
    if option == 9:
        main_menu()


def tones():
    print(f"""
      1. Ringing tone
      2. Ringing volume
      3. Incoming call alert
      4. Composer
      5. Message alert tone
      6. Keypad tones
      7. Warning and game tone
      8. Vibrating alert
      9. Screen saver
      10. Back""")
    option = int(input("Enter your option:  "))
    if option == 10:
        main_menu()


def restore_factory_settings():
    print(f"""
            1. Previous
            2. Main menu""")
    option = int(input("Enter your option:  "))
    if option == 1:
        settings()
    if option == 2:
        main_menu()


def security_settings():
    print("""
          1. PIN code request
          2. Call barring service
          3. Fixed dialling
          4. Closed user group
          5. Phone security
          6. Change access codes
          7. Back to settings
          8. Main menu""")
    option = int(input("Enter your option:  "))
    if option == 7:
        settings()
    elif option == 8:
        main_menu()
    else:
        print('Invalid option')
        message_settings()


def phone_settings():
    print(f"""
             1. Language
             2. Cell info display
             3. Welcome note
             4. Network selection
             5. Lights
             6. Confirm SIM service actions 
             7. Back to settings
             8. Main menu""")
    option = int(input("Enter your option:  "))
    if option == 7:
        settings()
    elif option == 8:
        main_menu()
    else:
        print('Invalid option')
        message_settings()


def call_settings():
    print(f"""
            1. Automatic redial
            2. Speed dialling
            3. Call waiting options
            4. Own number sending
            5. Phone line in use
            6. Automatic answer
            7. Back to settings
            8. Main menu""")
    option = int(input("Enter your option:  "))
    if option == 7:
        settings()
    elif option == 8:
        main_menu()
    else:
        print('Invalid option')
        message_settings()


def settings():
    print(f"""
        1. Call settings
        2. Phone settings
        3. Security settings
        4. Restore factory settings
        5. main menu""")
    option = int(input("Enter your option:  "))
    if option == 5:
        main_menu()
    if option == 1:
        call_settings()
    if option == 2:
        phone_settings()
    if option == 3:
        security_settings()
    else:
        print('Invalid option')
        settings()



def call_divert():
    print(f"""
        Call divert
        1. Back""")
    option = int(input("Enter your option:  "))
    if option == 1:
        main_menu()


def games():
    print(f"""
        games
        1. Back""")
    option = int(input("Enter your option:  "))
    if option == 1:
        main_menu()


def calculator():
    print(f"""
        calculator
        0. Back""")
    option = int(input("Enter your option:  "))
    if option == 0:
        main_menu()


def reminders():
    print(f"""
        reminder
        1. Back""")
    option = int(input("Enter your option:  "))
    if option == 1:
        main_menu()


def clock():
    print(f"""
        1. Alarm clock
        2. Clock settings
        3. Date setting
        4. Stopwatch
        5. Countdown timer
        6. Auto update of date and time
        7. Main menu""")
    option = int(input("Enter your option:  "))
    if option == 7:
        main_menu()


def profiles():
    print(f"""
        profiles
        1. Back""")
    option = int(input("Enter your option:  "))
    if option == 1:
        main_menu()


def sim_services():
    print(f"""
        SIM services
        1. Back""")
    option = int(input("Enter your option:  "))
    if option == 1:
        main_menu()


main_menu()
