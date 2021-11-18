"""
Provide a class for a deck of cards

Usage:

from carddeck import CardDeck

c = CardDeck("DealerName")
c.shuffle()
card = c.draw()
"""
class CardDeck:  # inherits from 'object' class
    def __init__(self, dealer):
        # self.dealer = dealer  # calls line 25
        self.dealer_name = dealer  # call the property
        # self.any_name = value  adds data to the instance

    #  dealer_name  public, property
    #  _dealer private, variable (not property)

    @property
    def dealer_name(self):   # getter property
        return self._dealer

    @dealer_name.setter
    def dealer_name(self, dealer):  # setter property
        if isinstance(dealer, str):
            self._dealer = dealer
        else:
            wrong_type = type(dealer).__name__
            raise TypeError(f"Dealer must be a str, not a {wrong_type}")









