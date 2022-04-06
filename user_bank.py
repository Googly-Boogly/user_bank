from pprint import pprint
class BankAccount:
    all_acs = []
    def __init__(self, amount, int, name):
        self.name = name
        self.balance = amount
        self.intrest = int
        BankAccount.all_acs.append(self.balance)
    def deposit(self, amount):
        self.balance += amount
    def withdraw(self, amount):
        if self.balance > amount:
            self.balance -= amount
        else:
            print('you aint got no money so im taking 5 bucks')
            self.balance -= 5
    def display_account_info(self):
        print(f'you have {self.balance}$')
    def yield_intrest(self):
        if self.balance > 0:
            self.balance = self.balance * self.intrest
        else:
            print('sorry ur broke')
    @classmethod
    def printt(cls):
        new_arr = []
        x = 0
        while x < len(cls.all_acs):
            new_arr.append(f'Balance: {round(cls.all_acs[x].balance)}$')
            x += 1
        pprint(new_arr)
class User:
    total_users = []
    def __init__(self,first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.entry = len(User.total_users)
        print('account number is 1')
        balance = int(input('How much money you want? '))
        int_rate = 1.02
        count = 1
        self.acc1 = BankAccount(amount=balance, int=int_rate, name=self.first_name)
        x = input('Do you want to make another account Y/N ')
        if x =='Y' or x == 'y':
            print('account number is 2')
            balance = int(input('How much money you want? '))
            int_rate = 1.02
            self.acc2 = BankAccount(amount=balance, int=int_rate, name=self.first_name)
            count = 2
        x = input('Do you want to make another account Y/N ')
        if x == 'Y' or x == 'y':
            print('account number is 3')
            balance = int(input('How much money you want? '))
            int_rate = 1.02
            self.acc3 = BankAccount(amount=balance, int=int_rate, name=self.first_name)
            count = 3
        if count == 1:
            User.total_users.append([self.first_name, self.entry, self.acc1])
        elif count == 2:
            User.total_users.append([self.first_name, self.entry, self.acc1, self.acc2])
        else:
            User.total_users.append([self.first_name, self.entry, self.acc1, self.acc2, self.acc3])
        # self.account = BankAccount(amount=0, int=1.02)

    def make_withdrawl(self, amount):
        x = int(input('What is the account number? '))
        if x == 1:
            x = self.acc1
        elif x == 2:
            x = self.acc2
        else:
            x = self.acc3
        if x.balance >= amount:
            x.balance -= amount
            print(f'took {amount}$ out')
        else:
            print('not enough cash money')
    def deposit(self, amount):
        x = int(input('What is the account number? '))
        if x == 1:
            x = self.acc1
        elif x == 2:
            x = self.acc2
        else:
            x = self.acc3
        x.balance += amount
        print(f'deposited {amount}$')
    def display_user_balance(self):
        x = int(input('What is the account number? '))
        if x == 1:
            x = self.acc1
        elif x == 2:
            x = self.acc2
        else:
            x = self.acc3
        print(f'User: {self.first_name} {self.last_name}, you have {x.balance}$ wow you are rich')
    def transfer_money(self, target, amount):
        x = int(input('What is the account number? '))
        if x == 1:
            x = self.acc1
        elif x == 2:
            x = self.acc2
        else:
            x = self.acc3
        if x.balance >= amount:
            x.balance -= amount
            target.acc1.balance = target.acc1.balance + amount
            print(f'{self.first_name} has {x.balance}$')
            print(f'{target.first_name} has {target.acc1.balance}$')


alex = User('Alex', 'G', 'A@gmail.com')
greg = User('Greg', 'T', 'G@gmail.com')
alex.deposit(5)
alex.make_withdrawl(1)
greg.transfer_money(alex, 7)
alex.display_user_balance()