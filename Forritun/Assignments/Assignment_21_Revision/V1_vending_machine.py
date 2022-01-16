# You have invented a vending machine capable of dispensing candies. Write a program to simulate the vending machine. It costs $1.50 to buy a packet of candies, and the machine only takes coins in denominations of a dollar (100 cents), quarter (25 cents), dime (10 cents), or nickel (5 cents). Write code to simulate a person putting money into the vending machine by repeatedly prompting the user for the next coin to be inserted. Output the total entered so far when each coin is inserted. When $1.50 or more is added, the program should output "Enjoy your candies. Your change is $x.xx. Please visit again." . Use functions and remember that each function should have a specific role. You will need to use the tab charcter(\t) to indent the options menu.

def output():
  amount = 0.00
  change = 1.50
  n = 0.05
  d = 0.10
  q = 0.25
  D = 1.00
  
  while amount < 1.50:
    print("A packet of candy costs $ 1.50. You have inserted $ {:.2f}.".format(amount))
    print("Please insert coins:")
    print("\tn - Nickel")
    print("\td - Dime")
    print("\tq - Quarter")
    print("\tD - Dollar")
    choice = input("")

    if choice == "n":
      amount += n
    elif choice == "d":
      amount += d
    elif choice == "q":
      amount += q
    elif choice == "D":
      amount += D
    else:
      print("'{}' is not a valid coin.".format(choice))

    if amount >= change:
      returned = amount - change
      print("Enjoy your candies. Your change is $ {:.2f}. Please visit again".format(returned))


output()
