# Question 5: Game of eights
# Write a function called 'game_of_eights()' that accepts a list of numbers as an argument and then returns 'True' if two consecutive eights are found in the list. For example: [2,3,8,8,9] -> True.
# The main() function will accept a list of numbers separated by commas from the user and send it to the game_of_eights() function. 
# The main() function prints out an error message saying 'Error. Please enter only integers.' if the list is found to contain any non-numeric characters. 

def game_of_eights(a_new):
  for i in range(len(a_new)-1):
    if(a_new[i]==8) and (a_new[i+1]==8):
      return True
  return False
    

def main():
  a_list = input("Enter elements of list separated by commas: ").split(',')
  try:
    a_new = [int(i) for i in a_list]
  except:
    print("Error. Please enter only integers.")
        
  print(game_of_eights(a_new))
  
main()
