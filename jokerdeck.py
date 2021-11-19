from carddeck import CardDeck
from card import Card

JOKER_NAME = "JOKER"

class JokerDeck(CardDeck):

    def _make_deck(self):
        super()._make_deck() # call in parent class
        for joker_number in '1', '2':
            card = Card(joker_number, JOKER_NAME)
            self._cards.append(card)

