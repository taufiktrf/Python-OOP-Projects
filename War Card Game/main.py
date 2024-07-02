from Suit import Suit
from Card import Card
from Deck import Deck
from Player import Player
from war_card_game import WarCardGame


player = Player("YOUR NAME", Deck(is_empty=True))
computer = Player("COMPUTER", Deck(is_empty=True), is_computer=True)
deck = Deck()

game = WarCardGame(player, computer, deck)

game.print_welcome_message()

while not game.check_game_over():
    game.start_battle()
    game.print_stats()

    ans = input("Press ENTER to continue || Press 'x' to stop")

    if ans.lower() == 'x':
        break