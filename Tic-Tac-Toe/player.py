import random
from move import Move


class Player:


    PLAYER_MARKER = "X"
    COMPUTER_MARKER = "O"


    def __init__(self, is_human=True) -> None:
        self._is_human = is_human

        if is_human:
            self._marker = Player.PLAYER_MARKER
        
        else:
            self._marker = Player.COMPUTER_MARKER


    property 
    def marker(self):
        return self._marker
    

    property 
    def is_human(self):
        return self._is_human
    

    def get_move(self):
        if self._is_human:
            return self.get_human_move()
        else:
            return self.get_computer_move()
        

    def get_human_move(self):
        while True:
            user_input = int(input("Please Enter Your Move (1-9):  "))
            move = Move(user_input)
            if move.is_valid():
                break
            else:
                print("Number not in (1-9)")

        return move
    

    def get_computer_move(self):
        random_choice = random.choice(list(range(1, 10)))
        move = Move(random_choice)
        print(f"Computer Move: {move.value}")

        return move