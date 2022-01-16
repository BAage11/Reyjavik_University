
class Chess_Players():

    def __init__(self, name, year, rating):
        self.name = name
        self.year = year
        self.rating = rating

    def __str__(self):
        return "Name: {}\nYear: {}\nRating: {}".format(self.name,self.year,self.rating)

    def __gt__(self, other): 
        return self.rating > other.rating


def read_players():
    name = input("Enter name: ")
    year = int(input("Enter year: "))
    rating = int(input("Enter rating: "))
    print()
    return name, year, rating


def get_highest_rated_player(players):
    return max(players)

        
def get_average_rating(players):
    sum_of = 0 
    for player in players: 
        sum_of += player.rating
    average = sum_of / len(players)
    return "{:.2f}".format(average)
        






def main():
    
    number_of_players = int(input("Number of players: "))
    players = []
    
    print("--- Reading players ---")
    #here you should get info from the user about 
    #number_of_players many chess player
    # code goes here....
    for x in range(number_of_players):
        name, year, rating = read_players()
        new_player = Chess_Players(name,year,rating)
        players.append(new_player)

    
    print("--- Displaying players --- ")
    #here you should print each player
    #code goes here....
    for player in players:
        print(player)
        print()

    highest_rated_player = get_highest_rated_player(players)
    print("Highest rated player: ")
    print(highest_rated_player)

    average_rating = get_average_rating(players)
    print("Average rating:", average_rating)




    
main()