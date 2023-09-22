# class TicTacToe:
#     def __init__(self):
#         self.board = [' ' for i in range(9)]
#
#     def display(self):
#         print("%s | %s | %s" % (self.board[0], self.board[1], self.board[2]))
#         print("%s | %s | %s" % (self.board[3], self.board[4], self.board[5]))
#         print("%s | %s | %s" % (self.board[6], self.board[7], self.board[8]))
#
#     def update(self, board_no, player_input):
#         if self.board[board_no] == "":
#             self.board[board_no] = player_input
#
#     def current_winner(self, player_input):
#         if self.board[1] == player_input and self.board[2] == player_input and self.board[3] == player_input:
#             return True
#
#
# tictactoe = TicTacToe()
#
#
# def header():
#     print("Welcome to Tic-Tac-Toe\n")
#
#
# def refresh_screen():
#     header()
#     tictactoe.display()
#
#
# while True:
#     refresh_screen()
#     x_choice = int(input("\nX) Enter a position 1 through 9 or enter 0 to quit:  "))
#     tictactoe.update(x_choice, "X")
#
#     refresh_screen()
#     if tictactoe.current_winner("X"):
#         print("X wins")
#         play_again = input("Play again? (yes/no")
#         if play_again == "y":
#             continue
#         else:
#             break
#
#     o_choice = int(input("\nO)Enter a position 1 through 9 or enter 0 to quit:  "))
#     tictactoe.update(o_choice, "O")
#
# tictactoe.display()
#
# # @staticmethod
# # def create_board(board):
# #     for row in board:
# #         for box in row:
# #             print(box + " ", end="")
# #         print()
# # #
# # def player_input(self):
# #     while True:
# #         user_input = input("Enter a position 1 through 9 or enter 0 to quit:  ")
# #         if user_input == "0":
# #             print("Thanks for playing")
# #             return True
# #         else:
# #             return False
# #
# # def check_user_input(self, user_input):
# #     if not user_input.isDigit():
# #         print("Number not valid")
# #         return False
# #     else:
# #         return True
#
#
# # def create_board(self):
# #     for i in range(3):
# #         row = []
# #         for j in range(3):
# #             row.append('_')
# #         self.board.append(row)
# #
# # def getPlayer(self):
