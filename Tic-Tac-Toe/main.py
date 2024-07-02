from move import Move
from board import Board
from player import Player

class TicTacToe:


    def start_new_round(self, board):
        print('******************')
        print('STARTING NEW ROUND')
        print('******************')

        board.reset_board()
        board.print_board()


    def start(self):
        print("**********************")
        print("Welcome to TIC-TAC-TOE")
        print("**********************")
        print()
        


        board = Board()
        player = Player()
        computer = Player(False)
        board.print_board_with_positions()
        print()

        while True: #GAME
            
            while True: #CURRENT_ROUND

                player_move = player.get_move()
                board.submit_move(player, player_move)
                board.print_board()

                if board.check_if_tie():

                    print("It's a TIE")
                    break
                elif board.check_if_game_over(player, player_move):
                    print("You Won the Game")
                    break
                else:

                    computer_move = computer.get_move()
                    board.submit_move(computer, computer_move)
                    board.print_board()

                    if board.check_if_game_over(computer, computer_move):
                        print("THE COMPUTER WON")
                        break

            play_again = input("\nTo play again, Enter 'X', else enter 'O' to STOP\n").upper()
            if play_again == 'O':
                print("BYE, COME BACK SOON")
                break

            elif play_again == 'X':
                self.start_new_round(board)
            else:
                print("\nYOUR INPUT IS NOT VALID --> STARTING NEW ROUND\n")
                self.start_new_round(board)

            


                
game = TicTacToe()
game.start()