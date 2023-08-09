def names_starting_with_s(names):
    new_dict = {}

    for name in names:
        name = name.capitalize()
        if name.startswith("S"):
            if name in new_dict:
                new_dict[name] += 1
            else:
                new_dict[name] = 1
    return new_dict


names = ["Samantha", "Daniel", "Seyi", "Kelvin", "Samantha", "Hakimi", "Segun", "Ashley", "seyi"]
print(names_starting_with_s(names))

#     #check = 'S'
#    # new_dict = [index for index in names if index[0].lower() == check.lower()]
#     return new_dict
#
#
