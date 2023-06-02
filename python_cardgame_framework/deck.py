""" A hand that can shuffle and deal """
from hand import Hand
from card import RANKS, SUITS, Card

class Deck(Hand):
    """A deck of playing cards"""

    def __init__(self):
        super().__init__()
        self.populate()

    def populate(self):
        """create a new deck of cards"""
        for rank in RANKS:
            for suit in SUITS:
                card = Card(rank, suit)
                self.add(card)


    def shuffle(self):
        """shuffles all cards in the hand
        
        Algorithm 1:
        GET deck (list or array) 
        INIT shuffled_deck (list or array) 
        FOR length(deck): 
            INIT chosen_card as range(deck) 
            APPEND shuffled_deck with chosen_card 
            REMOVE chosen_card from deck 
        Return shuffled_deck

        Algorithm 2:
        REPEAT half length of list
            SET position to random number between 0 and length of list
            REMOVE card from deck at position
            APPEND card to end of list.
        ENDREPEAT

        Algorithm 3:
        SET shuffled to empty list
        WHILE deck is not empty
            REMOVE (pop) card from random position in deck
            APPEND card to shuffled
        SET deck to shuffled
        """
        pass


if __name__ == "__main__":
    new_deck = Deck()
    print(new_deck)