class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    @property
    def rank(self):
        return self._rank

    @rank.setter
    def rank(self, value):
        self._rank = value

    @property
    def suit(self):
        return self._suit

    @suit.setter
    def suit(self, value):
        self._suit = value

    # human-friendly info
    def __str__(self):
        return f"{self.rank}-{self.suit}"

    # how to recreate the object (code-friendly)
    def __repr__(self):
        return f"Card('{self.rank}', '{self.suit}')"

