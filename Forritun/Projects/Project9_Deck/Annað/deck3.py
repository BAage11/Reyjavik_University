import random

class Deck():
  def __init__(self, hand1="", hand2="", hand3="", hand4=""):
    self.deck = []
    self.rank_str = ("A","2","3","4","5","6","7","8","9","10","J","Q","K")
    self.suit_str = ("S","H","D","C")
    for suit in self.rank_str:
      for rank in self.suit_str:
        card = suit+rank
        self.deck.append(card)

  def shuffle(self):
    pass
  
  def deal(self):
    pass

  def __str__(self):
    counter = 1
    cards = ""
    while counter <= 52:
      for i in self.deck:
        cards += (i + " ")
        counter += 1
    return cards


random.seed(10)
deck = Deck()
deck.shuffle()
print("The deck:")
print(deck)