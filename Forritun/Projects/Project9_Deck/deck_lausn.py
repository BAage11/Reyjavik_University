import random

class Card(object):
    """ A card with rank and suit """
    def __set_rank(self,rank):
        ''' Sets the rank of the card.  The rank parameter can either be
            a character or an integer corresponding to the rank.
            Internally, the rank is an integer.
        '''
        # rank is int: 1=Ace, 2-10 face value, 11=Jack, 12=Queen, 13=King
        self.__rank = 0 # Create a 0 rank as default
        if type(rank) == str:
            if rank in 'Jj':
                self.__rank = 11  # Jack
            elif rank in 'Qq':
                self.__rank = 12  # Queen
            elif rank in 'Kk':
                self.__rank = 13  # King
            elif rank in 'aA':
                self.__rank = 1   # Ace
        elif type(rank) == int:
            if 1 <= rank <= 14:
                self.__rank = rank

    def __set_suit(self, suit):
        ''' Sets the suit of the card.  Suit is a character 
            S=Space, H=Heart, D=Diamond, C=Club)
        '''
        self.__suit = '' # create blank suit by default
        if type(suit) == str and suit:
            if suit in 'Cc':
                self.__suit = 'C'
            elif suit in 'Hh':
                self.__suit = 'H'
            elif suit in 'Dd':
                self.__suit = 'D'
            elif suit in 'Ss':
                self.__suit = 'S'
        
    def is_blank(self):
        return self.__rank == 0 or self.__suit == ''
        
    def __init__(self, rank = 0, suit = ''): 
        if not (rank == 0 and suit == ''):
            self.__set_rank(rank)
            self.__set_suit(suit)
        else:
            self.__rank = 0
            self.__suit = ''
        
    def __str__(self):
        """
            String representation of card for printing: rank + suit,
            e.g. 7S or JD, 'blk' for 'no card'
        """
        name_string = "blk A 2 3 4 5 6 7 8 9 10 J Q K"  # 'blk' for blank, i.e. no card
        name_list = name_string.split()   # create a list of names so we can index into it using rank
            
        return ("{:>3s}".format(name_list[self.__rank]+self.__suit))

class Deck(object):
    """ A deck to play cards with """
    NUMBER_CARDS_LINE = 13
    def __init__(self):
        """ Initialize deck as a list of all 52 cards: 13 cards in each of 4 suits """
        self.__deck = [Card(i, j) for i in range(1,14) for j in "SHDC" ] # list comprehension
        
    def __str__(self):
        """ Represent the whole deck as a string for printing """
        s = ""
        for index, card in enumerate(self.__deck):
            if index % Deck.NUMBER_CARDS_LINE == 0 and index != 0:  # insert newline: print 13 cards per line
                s += "\n"  
            s += str(card) + " "
        return s

    def shuffle(self):
        """ Shuffle the deck """
        random.shuffle(self.__deck) # random.shuffle() randomly rearranges a sequence

    def deal(self):
        """ Deal a single card by returning the card that is removed off the top of the deck """
        if len(self.__deck) == 0:  # deck is empty
            return None
        else:
            return self.__deck.pop(0)  # remove card (pop it) and then return it
  

class PlayingHand(object):
    NUMBER_CARDS = 13
    def __init__(self):
        """ Initializes an empty playing hand """
        self.__cards = [ Card() for i in range(PlayingHand.NUMBER_CARDS)] 

    def __str__(self):
        """ Represent the whole hand as a string for printing """
        s = ""
        for card in self.__cards:
            s += str(card) + " "
        return s

    def add_card(self, a_card):
        ''' Adds the given card to the hand '''
        # Find the empty slot the card
        empty_idx = -1
        for idx, card in enumerate(self.__cards):
            if (card.is_blank()):
                empty_idx = idx
                break
        # Add the card if an empty slot is founds
        if empty_idx >= 0:
            self.__cards[empty_idx] = a_card

def test_cards():
    card1 = Card()
    print(card1)
    card2 = Card(5,'s')
    print(card2)
    card3 = Card('Q','D')
    print(card3)
    card4 = Card('x', 7)
    print(card4)
    
def print_4_hands(hand1, hand2, hand3, hand4):
    ''' Prints the 4 hands '''
    print(hand1)
    print(hand2)
    print(hand3)
    print(hand4)

def deal_4_hands(deck, hand1, hand2, hand3, hand4):
    ''' Deals cards for 4 hands '''
    for _ in range(PlayingHand.NUMBER_CARDS):
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
