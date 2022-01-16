# In golf, pars for a hole range from 3 to 5.  Write a program using a while statement that allows the user to input the par and the score for each of the 18 holes. Based on the number of shots compared to par, the program writes out the following:
# •	"invalid score", for less than 3 under par
# •	"albatross", for 3 under par
# •	"eagle", for 2 under par
# •	"birdie", for 1 under par
# •	"bogey", for 1 over par
# •	"double bogey", for 2 over par
# •	"triple bogey", for 3 over par
# •	"bad hole", for scores more than 3 over par

hole = 1
while hole <= 18:
  par = int(input("Par of hole: "))
  score = int(input("Score on hole: "))

  if score < (par - 3):
    print("invalid score")
  elif score == par:
    print("par")
  elif score == par - 3:
    print("albatross")
  elif score == par - 2:
    print("eagle")
  elif score == par - 1:
    print("birdie")
  elif score == par + 1:
    print("bogey")
  elif score == par + 2:
    print("double bogey")
  elif score == par + 3:
    print("triple bogey")
  elif score > par + 3:
    print("bad hole")
  
  hole += 1
