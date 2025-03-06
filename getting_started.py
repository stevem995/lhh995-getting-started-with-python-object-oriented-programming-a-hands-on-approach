"""
Python Object-Oriented LHH Linkedin learning Programming class
Geting started with PYthon object Oriented Programming: A hands on approach
"""

class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __repr__(self):
        return f"{self.value} of {self.suit}"
       
if __name__ == "__main__":
    card1 = Card("Ace", "Spades")
    card2 = Card("Queen", "Hearts")

    print("{}".format(card1))
    print("{}".format(card2))
