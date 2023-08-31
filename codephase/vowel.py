import re


def vowel(list_of_letters) -> str:
    while True:
        letters = input("Enter a letter:  ")
        if re.search(r'[aeiou]', letters):
            print("letter is a vowel")
        else:
            print("letter is not a vowel")


print(vowel('list_of_letters'))
