"""
Provide a class for a deck of cards

Usage:

from carddeck import CardDeck

c = CardDeck("DealerName")
c.shuffle()
card = c.draw()
"""
import random
from card import Card


class CardDeck:  # inherits from 'object' class
    SUITS = 'Clubs Diamonds Hearts Spades'.split()
    RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()

    def __init__(self, dealer):
        # self.dealer = dealer  # calls line 25
        self.dealer_name = dealer  # call the property
        # self.any_name = value  adds data to the instance
        self._make_deck()

    #  dealer_name  public, property
    #  _dealer private, variable (not property)

    def _make_deck(self):
        self._cards = list()
        for suit in self.SUITS:
            for rank in self.RANKS:
                card = Card(rank, suit)
                self._cards.append(card)


    @property
    def cards(self):
        return self._cards


    def shuffle(self):
        random.shuffle(self._cards)


    def draw(self):
        return self._cards.pop()

    @property
    def dealer_name(self):   # getter property
        return self._dealer

    # dealer_name = property(dealer_name)

    @dealer_name.setter
    def dealer_name(self, dealer):  # setter property
        if isinstance(dealer, str):
            self._dealer = dealer
        else:
            wrong_type = type(dealer).__name__
            raise TypeError(f"Dealer must be a str, not a {wrong_type}")

    def __repr__(self):
        my_type = type(self)
        my_name = my_type.__name__

        return f"{my_name}('{self.dealer_name}')"






