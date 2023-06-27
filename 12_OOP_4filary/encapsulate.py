class Account:
    def __init__(self, first_name, last_name):
      self.first_name = first_name
      self.last_name = last_name
      self.__account_number = '12 4530 0000 1001 2345 3213'

    def show_number(self):
        print(f"You bank account numer: {self.__account_number}")

    def set_new_number(self, new_number):
        self.__account_number = new_number


user_account = Account('Jon', 'Snow')
print("user name:", user_account.first_name)
user_account.show_number()
user_account.first_name = "John"
print("user name:", user_account.first_name)
print("pronuje zmodyfikować nr")
user_account.set_new_number("10 0000 000 0000")
user_account.show_number()
