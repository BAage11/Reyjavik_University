RANK = 0
COUNTRY = 1
RATING = 2
BYEAR = 3
NUM_ATTRIBUTES = 4

def create_players_dict(filename):
  the_dict = {}
  def get_value_list():
    """ Return a list of the given values. """
    a_list = [None] * NUM_ATTRIBUTES
    a_list[RANK] = int(rank)
    a_list[COUNTRY] = country.strip()
    a_list[RATING] = int(rating)
    a_list[BYEAR] = int(byear)
    return a_list
  try:
    file_stream = open(filename, "r")
    for line in file_stream:
      rank, name, country, rating, byear = line.split(";")
      lastname, firstname = name.split(",")
    # Save name, remaining data as (key,value) in dict
      key = "{}{}".format(firstname, lastname).strip()
      value_list = get_value_list()  
             # value_list = [int(rank), country, int(rating), int(byear)]
      the_dict[key] = value_list  
    file_stream.close()
  except FileNotFoundError:
    pass 
  return the_dict

def create_attribute_dict(dict_players, attribute_key):
  the_dict = {}
  for chess_player,chess_player_data in dict_players.items():
    key = chess_player_data[attribute_key]      #   Extract name and country
    if key in the_dict:       #   Add (or append) name as a value for the country key
      name_list = the_dict[key]
      name_list.append(chess_player)
    else:
      name_list = [chess_player]
      the_dict[key] = name_list
  return the_dict

def get_average_rating(players, dict_players):
  """ Return the average rating for the given players. """
  ratings = [ dict_players[player][RATING] for player in players]
  average = sum(ratings) / len(ratings)
  return average

def print_sorted(the_dict, dict_players):
  # loop through sorted dict_countries
  sorted_tuples = sorted(the_dict.items())
  #  Extract number of players in country
  #  Compute the average rating of each country
  for key,players in sorted_tuples:
    average = get_average_rating(players, dict_players)
    print("{} ({}) ({:.1f}):".format(key, len(players), average))
  #  For each player, print name and rating
    for player in players:
      rating = dict_players[player][RATING]
      print("{:>40s}{:>10d}".format(player, rating))

def print_header(header_str):
  print(header_str)
  dashes = "-" * len(header_str)
  print(dashes)


# The main program starts here:
filename = input("Enter filename: ")
dict_players = create_players_dict(filename)

dict_countries = create_attribute_dict(dict_players, COUNTRY)
print_header("Players by country:")
print_sorted(dict_countries, dict_players)
print("\n")
dict_years = create_attribute_dict(dict_players, BYEAR)
print_header("Players by birth year:")
print_sorted(dict_years, dict_players)
