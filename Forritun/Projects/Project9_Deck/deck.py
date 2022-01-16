import random

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
  
  def deal(self):  
    return self.deck.pop(0)

  def __str__(self):
    cards = []
    for i in self.deck:
      cards.append(i)
    return " {}\n {}\n {}\n {}".format(" ".join(cards[0:13]), " ".join(cards[13:26]), " ".join(cards[26:39]), " ".join(cards[39:52]))


class PlayingHand():
  NUMBER_CARDS = 13
  def __init__(self, hand=""):
    self.hand = [str(Card()) for x in range(PlayingHand.NUMBER_CARDS)]

  def add_card(self, card):
    for i,v in enumerate(self.hand):
      if v == "blk":
        self.hand[i] = card
        break

  def __str__(self):
    print_hand = ""
    for j in self.hand:
      print_hand += "{:>3} ".format(j)
    return print_hand


###################################################################

def test_cards():
  card1 = Card()
  print(card1)
  card2 = Card(5,"S")
  print(card2)
  card3 = Card("Q", "D")
  print(card3)
  card4 = Card("x", 7)
  print(card4)

def print_4_hands(hand1, hand2, hand3, hand4):
  """ Prints the 4 hands """
  print(hand1)
  print(hand2)
  print(hand3)
  print(hand4)

def deal_4_hands(deck, hand1, hand2, hand3, hand4):
  """ Deals cards for 4 hands """
  for i in range(PlayingHand.NUMBER_CARDS):
    hand1.add_card(deck.deal())
    hand2.add_card(deck.deal())
    hand3.add_card(deck.deal())
    hand4.add_card(deck.deal())

def test_hands(deck):
  hand1 = PlayingHand()
  hand2 = PlayingHand()
  hand3 = PlayingHand()
  hand4 = PlayingHand()
  print("The 4 hands:")
  print_4_hands(hand1, hand2, hand3, hand4)

  deal_4_hands(deck, hand1, hand2, hand3, hand4)
  print("The 4 hands after dealing:")
  print_4_hands(hand1, hand2, hand3, hand4)


# The main program starts here
random.seed(10)
test_cards()

deck = Deck()
deck.shuffle()
print("The deck:")
print(deck)

test_hands(deck)
print("The deck after dealing:")
print(deck)
