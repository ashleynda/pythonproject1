class IncorrectNameException(Exception):
    def __init__(self, message):
        self.message = message
        super.__init__(message)


class IncorrectPinException(Exception):
    def __init__(self, message):
        self.message = message
        super.__init__(message)
