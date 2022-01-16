def print_table(dimen):
  counter = 0
  for inner_list in table:
    for value in inner_list:
      print("{:>5} ".format(value), end = "")
      counter += 1
      if counter == dimen:
        print()
        counter = 0

def make_table(dimen):
  counter = 0
  for num in range(dimen):
    a_list = []
    a_list = [x + dimen*counter for x in range(1, dimen + 1)]
    counter += 1
    table.append(a_list)

def turn_XO(dimen,team):
  position = int(input("{} position: ".format(team)))
  for y in range(dimen):
    for x in range(dimen):
      if table[y][x] == position:
        table[y][x] = team
        return True
  return False

def find_active_player(active_player):
  team1 = "X"
  team2 = "O"
  if active_player == team1:
    active_player = team2
    return active_player
  else:
    active_player = team1
    return active_player

def keep_playing(dimen,team):
  counter1 = 0
  counter2 = 0
  counter3 = 0
  counter4 = 0
  for y in range(dimen):              #Checks if x(inner) values in list are all X/O's
    for x in range(dimen):
      if table[y][x] != team:
        break
      else:
        counter1 += 1
  for x in range(dimen):              #Checks if y values in list are all X/O's
    counter2 = 0
    for y in range(dimen):
      if table[y][x] != team:
        break
      else:
        counter2 += 1
  for x in range(dimen):              #Checks diagonally to right
    if table[x][x] != team:
      break
    else:
      counter3 += 1
  y = 0
  for x in range(dimen):             #Checks diagonally to left
    y-=1
    if table[y][x] != team:
      break
    else:
      counter4 += 1
  if counter1 == dimen or counter2 == dimen or counter3 == dimen or counter4 == dimen:
    print("Winner is:",team)
    return True
  return False

def table_full(dimen):
  counter = 0
  for y in range(dimen):              #Checks if x(inner) values in list are all X/O's
    for x in range(dimen):
      if table[y][x] == "X" or table[y][x] == "O":
        counter += 1
  if counter == dimen**2:
    print("Draw!")
    return True
  return False

def play_game(dimen,active_player):
  stop = False
  while stop is False:
    valid = False
    active_player = find_active_player(active_player)
    while valid is False:
      try:
        valid = turn_XO(dimen,active_player)
      except:
        print("Illegal move!")
      if valid is False:
        print("Illegal move!")
    print_table(dimen)
    stop = keep_playing(dimen,active_player)
    if stop is False:
      stop = table_full(dimen)

def main():
  active_player = "O"
  dimen = int(input("Input dimension of the board: "))
  make_table(dimen)
  print_table(dimen)
  play_game(dimen,active_player)

table = []
main()

#https://github.com/MaggaSK97/Skil7