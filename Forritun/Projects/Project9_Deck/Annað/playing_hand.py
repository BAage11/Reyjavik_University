class PlayingHand():
  def __init__(self, hand1="", hand2="", hand3="", hand4=""):
    self.hand1 = hand1
    self.hand2 = hand2
    self.hand3 = hand3
    self.hand4 = hand4

  def __str__(self):
    if self.hand1 == False:
      self.hand1 = "blk"
    if self.hand2 == False:
      self.hand2 = "blk"
    if self.hand3 == False:
      self.hand3 = "blk"
    if self.hand4 == False:
      self.hand4 = "blk"
    return "{} {} {} {}".format(self.hand1, self.hand2, self.hand3, self.hand4)



def print_4_hands(hand1, hand2, hand3, hand4):
  """ Prints the 4 hands """
  print(hand1)
  print(hand2)
  print(hand3)
  print(hand4)

# def deal_4_hands(deck, hand1, hand2, hand3, hand4):
#   """ Deals cards for 4 hands """
#   for i in range(PlayingHand.NUMBER_CARDS):
#     hand1.add_card(deck.deal())
#     hand2.add_card(deck.deal())
#     hand3.add_card(deck.deal())
#     hand4.add_card(deck.deal())

def test_hands(deck):
  hand1 = PlayingHand()
  hand2 = PlayingHand()
  hand3 = PlayingHand()
  hand4 = PlayingHand()
  print("The 4 hands:")
  print_4_hands(hand1, hand2, hand3, hand4)

#   deal_4_hands(deck, hand1, hand2, hand3, hand4)
#   print("The 4 hands after dealing:")
#   print_4_hands(hand1, hand2, hand3, hand4)


print_4_hands()
# deal_4_hands()
test_hands()
