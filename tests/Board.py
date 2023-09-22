class Board:
    def __init__(self):
        self.__isEmpty = True
        self.__board = ['--' for i in range(9)]

    def isEmpty(self) -> bool:
        for space in self.__board:
            if space != '--':
                self.__isEmpty = False
        return self.__isEmpty

    def move(self, player_no, spot):
        for new_counter in range(len(self.__board)):
            if (spot - 1) == new_counter:
                self.__board[new_counter] = player_no

    def isFilled(self):




# @dataclass(frozen=True)
# class Player:
#     name: str
#     sign: str

