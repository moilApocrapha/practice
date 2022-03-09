"""black jack game. create a deck, shuffle it, and have a dealer play with 3 players."""
import random
from time import sleep


class Deck(list):

    suits = ("Hearts", "Spades", "Diamonds", "Clubs")
    values = {"Ace": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "Jack": 10,
              "Queen": 10, "King": 10}

    def __init__(self):
        list.__init__(self)

        for suit in self.suits:
            for value in self.values.keys():
                self.append((f"{value} of {suit}", self.values[value]))

        random.shuffle(self)


class Player:

    def __init__(self, name, risk=0):

        self.name = name
        risk += 15
        if risk > 20:
            self.risk = 20
        elif risk < 10:
            self.risk = 10
        else:
            self.risk = risk
        self.cards = []
        self.score = 0
        self.blackjack = False
        self.stay = False
        self.bust = False

    def hit(self, card):

        if self.bust:
            print(f"Score is {self.score} Busted")
        elif self.stay:
            print(f"Score is {self.score}, I'm scared.")
        elif self.blackjack:
            print("BlackJack!")
        else:
            self.cards.append(card)
            if card[1] == 1 and self.score <= 10:
                self.score += 11
            else:
                self.score += card[1]

            if self.score == 21:
                self.blackjack = True
            elif self.score >= 21:
                self.bust = True
            elif self.score >= (self.risk):
                self.stay = True

    def hand(self):
        hand = [card[0] for card in self.cards]
        return hand


class Dealer(Player):

    deck = None

    def __init__(self, name, risk=0):
        Player.__init__(self, name, risk)
        self.deck = Deck()

    def deal(self, players):

        for player in players:
            if isinstance(player, Player):
                player.hit(self.deck.pop())

    def new_deck(self):
        self.deck = Deck()


if __name__ == "__main__":

    player1 = Player("Bobry")
    player2 = Player("Floyd", 3)
    player3 = Player("Jimothy", -2)
    dealer = Dealer("Mac", 4)
    table = (player1, player2, player3, dealer)

    start = False
    print(f"{player1.name}, {player2.name}, {player3.name}, and dealer {dealer.name}")
    print("are ready to play.\n")

    accept = ("y", "yes")
    deny = ("n", "no")
    res = None

    while (res not in accept) and (res not in deny):
        res = input("Start the game?  y/n: ").lower()

        if res in accept:
            start = True
            dealer.deal(table)
        elif res in deny:
            pass
        else:
            print("how about a real answer\n\n")

    while start:

        finished = []
        for player in table:
            if player.bust:
                print(f"{player.name} has busted")
                finished.append(True)
            elif player.blackjack:
                print(f"{player.name} has blackjack!")
                finished.append(True)
            elif player.stay:
                print(f"{player.name} has decide to stay at {player.score}")
                finished.append(True)
            else:
                player.hit(dealer.deck.pop())
                print(f"{player.name} asks for a card")
                finished.append(False)
            sleep(1)

        if False not in finished:
            start = False
        else:
            print(f"""\n\nEnd of round\n""")
            for player in table:
                print(f"{player.name}'s score: {player.score}; ", end="")
                for card in player.hand():
                    print(f" {card} ", end="")
                print()
            input("\npress a key to continue")

    winner = []
    [winner.append(player) for player in table if player.blackjack]
    if len(winner) == 0:
        score = (0, None)
        for player in table:
            if player.score > score[0] and not player.bust:
                score = (player.score, player)
        winner.append(score[1])


    print("\nGame results\n---------------------\n")
    for player in table:
        if player in winner:
            print(f"{player.name} is a winner with score {player.score}")
        else:
            print(f"{player.name} has lost with score {player.score}")











