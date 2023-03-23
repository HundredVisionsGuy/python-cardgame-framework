"""
Name: Card.py
Author: Chris Winikka
Purpose: Represents a card in a card game.
"""

class Card:
    """A card in a card game (can serve as a base class for other types of
    card games).

    This is a typical card from a Bicycle/Hoyle type card deck like you would
    use in a BlackJack, Poker type card game.

    Attributes:
        RANKS (tuple): possible card ranks (str)
        SUITS (tuple): possible card SUITs (str)
        rank (str): represents the current card's rank
        suit (str): the current card's suit
        is_showing (bool): can we see the rank and suit of a card
        """
    RANKS = ("Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack",
             "Queen", "King")
    SUITS = ("Clubs", "Hearts", "Spades", "Diamonds")

    def __init__(self, rank: str, suit: str) -> None:
        self.rank = rank
        self.suit = suit

if __name__ == "__main__":
    card1 = Card("Ace", "Spades")
    print(card1.rank)
    print(card1.suit)