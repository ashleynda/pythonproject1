class NonExistentAccount(Exception):

    def __init__(self, message):
        super().__init__(message)


class AmountNotEnoughException:

    def __init__(self, message):
        super().__init__(message)