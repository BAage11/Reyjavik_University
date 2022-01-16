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
    random.shuffle(self.deck)
    return
  
  def deal(self):    # ATHUGA BETUR
    return self.deck.pop(len(self.deck))

  def __str__(self):
    counter = 1
    cards = []
    while counter <= 52:
      for i in self.deck:
        cards.append(i)
        counter += 1
    return " {}\n {}\n {}\n {}".format(" ".join(cards[0:13]), " ".join(cards[13:26]), " ".join(cards[26:39]), " ".join(cards[39:52]))


random.seed(10)
deck = Deck()
deck.shuffle()
print("The deck:")
print(deck)