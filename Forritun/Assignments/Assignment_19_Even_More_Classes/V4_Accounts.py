# In this assignment you will help a new bank get up and running. The Bank is called Happy Bank and it has two kinds of accounts, a savings account and a debit account. You will need to use inheritance in this assignment so you will need to figure out what the account types have in common and what they don´t. The accounts should have a method called update_balance() which updates the balance.
# A savings account updates the balance as follows:
# It updates the balance by its interest rate and adds a bonus rate to it. For a savings account the interest rate is 5% and the bonus rate is 10%.
# A debet account updates the balance as follows:
# It updates the balance by its interest rate which is 2 % for debet accounts.
# HINT: think about using class variables for the constants (interest rate and bonus rate).
# You also need to implement the __str__() method. Think about where you should implement it. You only need to implement it once. Look at the output example here below to figure out what string the method should return.
# You also need to implement the functions print_accounts() which should print each account and update_accounts() which should call the method update_balance() on each account.

class Account():
  INTEREST_RATE = 0.0
  BONUS_RATE = 0.0
  def __init__(self, amount):
    self.amount = amount

  def __str__(self):
    return "Balance: {:.2f}".format(self.amount) 

  def update_balance(self):
    self.amount += (self.amount * self.INTEREST_RATE + self.amount * self.BONUS_RATE)


class SavingsAccount(Account):
  INTEREST_RATE = 0.05
  BONUS_RATE = 0.10
  def __init__(self, amount):
    Account.__init__(self, amount)


class DebitAccount(Account):
  INTEREST_RATE = 0.02
  BONUS_RATE = 0.00
  def __init__(self, amount):
    Account.__init__(self, amount)


def print_accounts(account):
  for i in account:
    print(i)

def update_accounts(account):
  for j in account:
    j.new_balance()

def main():
    s1 = SavingsAccount(1000)
    d1 = DebitAccount(1000)
    s2 = SavingsAccount(2000)
    d2 = DebitAccount(4000)

    accounts = [s1, d1, s2, d2]

    print_accounts(accounts)
    update_accounts(accounts)

    print_accounts(accounts)
    update_accounts(accounts)

    print_accounts(accounts)
    update_accounts(accounts)

main()