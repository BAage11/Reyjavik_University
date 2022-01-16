import random

def define_cards():
  rank_str = ("A","2","3","4","5","6","7","8","9","10","J","Q","K")
  suit_str = ("C","D","H","S")
  cards = []
  for suit in suit_str:
    for rank in rank_str:
      card = rank+suit
      cards.append(card)
  return cards

def create_deck(deck):
  for i in range(52):
    deck.append(i)
    return

def shuffle_deck(deck):
  random.shuffle(deck)
  return

# def deal_card(deck):
#     return deck.pop(0)

deck = define_cards()
shuffle_deck(deck)
print ("The deck:")
print(deck)