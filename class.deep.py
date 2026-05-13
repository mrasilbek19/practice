'''CLASS deep diving
     (1) ENCAPSULATION
     (2) INHERITANCE
     (3) POLIMORPHISM
'''
print("========= ENCAPSULATION ==========")
'''
C++, JAVA > public private protected
python > public, __private, _protected --> 1 underline protected, 2 underlines private, no underline public 
'''


class Account():
    # state
    description = "This class makes bank accounts"

    # constructor
    def __init__(self, owner, amount):
        self.__owner = owner
        self.__amount = amount

    # method
    def get_balance(self):
        print(f"the owner {self.__owner} has {self.__amount} usd")

    def deposit(self, amount):
        print("deposit money")
        self.__amount += amount

    def withdraw(self, amount):
        print("withdraw money")
        self.__amount -= amount

    # getter va setter methodlar
    # decoraterlardan foidalanib

    @property
    def holder(self):
        return self.__owner

    @holder.setter  # tepa bilan bir hil bulishi kerak
    def holder(self, new_owner):
        print("holder.setter:", new_owner)
        self.__owner = new_owner

    def change_ownership(self, new_owner):
        print("change_ownership: ", new_owner)
        self.__owner = new_owner


my_account = Account("Alex", 1000)

my_account.deposit(200)
my_account.withdraw(100)
my_account.get_balance()

print("-------------------")

my_account.owner = "Bob"  # no Change private
my_account.get_balance()

try:
    result = my_account.amount  # prrivate bulgani uchun tulliq yopiq
    print("result: ", result)
except Exception as err:
    print("No target state found", err)

print("-------------------")
account_owner = my_account.holder  # state (getter method)
print(account_owner)

my_account.holder = "Nick"  # setter ham state sifatida call buladi
print(my_account.holder)
