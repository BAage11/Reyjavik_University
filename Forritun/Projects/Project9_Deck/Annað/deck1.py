import random

class Deck():
  def __init__(self, hand1="", hand2="", hand3="", hand4=""):
    self.deck = ["AS", "AH", "AD", "AC", "2S", "2H", "2D", "2C", "3S", "3H", "3D", "3C", "4S", "4H", "4D", "4C", "5S", "5H", "5D", "5C", "6S", "6H", "6D", "6C", "7S", "7H", "7D", "7C", "8S", "8H", "8D", "8C", "9S", "9H", "9D", "9C", "10S", "10H", "10D", "10C", "JS", "JH", "JD", "JC", "QS", "QH", "QD", "QC", "KS", "KH", "KD", "KC",]
#    self.hand1 = hand1
#    self.hand2 = hand2
#    self.hand3 = hand3
#    self.hand4 = hand4
    self.card = self.deal()

  def shuffle(self):
    random.shuffle(self.deck)
    return

  def deal(self):
    dealt_cards = []
    self.card = ""
    counter = 1
    while counter <= 52:
      for i in self.shuffle():
        if i in dealt_cards:
          continue
        else:
          self.card = i
          dealt_cards.append(i)
          counter += 1
          return self.card

  def __str__(self):
    return "{}".format(self.card)
#    return "{:>3} \n {} \n {} \n {}".format(hand1, self.hand2, self.hand3, self.hand4)


random.seed(10)
deck = Deck()
deck.shuffle()
print("The deck:")
print(deck)
