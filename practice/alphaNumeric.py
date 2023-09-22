def alphanumeric(number, value):
    # input = ["dfa12321afd"]

    for elements in range(len(number)):
        highest = number[0]
        for higher in number:
            if higher <= highest:
                highest = higher
        return highest


print(alphanumeric("dfa12321afd"))
