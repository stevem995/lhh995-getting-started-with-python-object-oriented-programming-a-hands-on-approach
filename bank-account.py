"""
BankAccount class: Getting started with python object oriented programming.
Getters and Setters challenge: Create Setter for balance of account.
"""

class BankAccount:
    def __init__(self, account_number, account_holder, account_balance):
        self._account_number_private = account_number
        self.account_holder_public = account_holder
        self._balance_private = account_balance

    def get_account_number(self):
        return self._account_number_private

    def get_account_holder(self):
        return self._account_holder_public

    def get_account_balance(self):
        return self._account_balance_private

    # Setters
    def set_account_number(self, account_number):
        if isinstance(account_number, str):
            self._account_number_private = account_number
            print("my_account: {}".format(vars(self)))
        else:
            print("\n{}: Error: Account number must be a string!\n".format(self.__class__.__name__))

    def set_account_balance(self, account_balance):
        if not isinstance(account_balance, float):
            print("\n{}: Error: Account number must be a float!\n".format(self.__class__.__name__))
        else:
            if self._balance_private < 0:
              print("\n{}: Error: Balance is less than zero!\n".format(self.__class__.__name__))
            else:
              self._balance_private = account_balance
              print("my_account: {}".format(vars(self)))

if __name__ == "__main__":
    # Create an account
    my_account = BankAccount(432991383933, "John Doe", 1000.0)

    print("Account Number: {}".format(my_account._account_number_private))
    print("Account Holder: {}".format(my_account.account_holder_public))
    print("Account Balance: {}".format(my_account._balance_private))

    print("Seting new account number:")
    my_account.set_account_number("544220243849045")
    print("Seting new account balance:")
    my_account.set_account_balance(14.0)
