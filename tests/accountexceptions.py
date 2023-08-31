class InvalidAmountException(Exception):
    def __init__(self, message):
        super().__init__(message)


class InsufficientAmountException(Exception):

    def __init__(self, message):
        super().__init__(message)
