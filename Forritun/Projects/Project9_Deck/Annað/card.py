class Card():
  def __init__(self, rank=0, suit=""):
    self.rank = rank
    self.suit = suit

  def is_blank(self):
    ranks = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    suits = ["C", "H", "D", "S"]
    for i in ranks:
      if i == str(self.rank):
        return True
    for j in suits:
      if j == self.suit:
        return True
  
  def __str__(self):
    if self.rank == False or self.suit == False:
      return "blk"
    if self.is_blank() != True:
      return "blk"
    else:      
      return "{:>3}".format(str(self.rank)+str(self.suit))  


def test_cards():
  card1 = Card()
  print(card1)
  card2 = Card(5,"S")
  print(card2)
  card3 = Card("Q", "D")
  print(card3)
  card4 = Card("x", 7)
  print(card4)

test_cards()