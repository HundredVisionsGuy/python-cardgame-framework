"""A Hand of playing Card objects"""

class Hand:
    """a hand of playing cards

    You can do the following: add a card, give a card, or clear the hand
    
    Attributes:
        cards (list): a list of card objects"""

    # constructor
    def __init__(self):
        self.cards = []
    
    def add(self, card):
        self.cards.append(card)
    
    def give(self, card, other_hand):
        # remove that card from this hand
        self.cards.remove(card)
        # add that card to the other hand
        other_hand.add(card)
    
    def clear(self):
        self.cards = []
    
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

    def __str__(self):
        """print the cards, but only if the hand is not empty"""
        if self.cards:
            representation = ""
            for card in self.cards:
                if not card.is_showing:
                    card.flip()
                representation += str(card) + " | "
        else:
            representation = "<empty>"
        return representation
    
if __name__ == "__main__":
    import Card
    
    # create a hand
    deck = Hand()
    for rank in Card.RANKS:
        for suit in Card.SUITS:
            card = Card.Card(rank, suit)
            deck.add(card)
    print(deck)