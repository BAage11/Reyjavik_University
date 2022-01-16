# Write a program that reads in information about n chess players and stores them in a list(n is always greater than 1). A chess player has a name(a string), a birth year (an integer) and chess rating (an integer). A chessplayer should be implemented as a class. The program then displays the information about the chess players, finds and writes out the highest rated player (if two players have the same rating then the former one is considered higher) and writes out the average rating.
# You will need to implement the __str__ method in the class and you also need to override an operator.

class ChessPlayers():
  def __init__(self, name="", age=0, rating=0):
    self.name = name
    self.age = age
    self.rating = rating
   
  def __str__(self):
    return "Name: {}\nYear: {}\nRating: {}\n".format(self.name, self.age, self.rating)

  def __gt__(self, other):
    return self.rating > other.rating


def get_highest_rated_player(players):
  return max(players)

def get_average_rating(players):
  total = 0
  for x in players:
    total += int(x.rating)
  average = total / len(players)
  return "{:.2f}".format(average)


###########################################################

def main():
  number_of_players = int(input("Number of players: "))
  players = []
  
  print("--- Reading players ---")
  for i in range(number_of_players):
    name = input("Enter Name: ")
    age = input("Enter Year: ")
    rating = input("Enter Rating: ")
    players.append(ChessPlayers(name, age, rating))
    

  print("--- Displaying players ---")
  for i in players:
    print(i)

  highest_rated_player = get_highest_rated_player(players)
  print("Highest rated player: ")
  print(highest_rated_player)
  average_rating = get_average_rating(players)
  print("Average rating:", average_rating)

main()