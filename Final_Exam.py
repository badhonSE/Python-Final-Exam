import random

class User:
    def __init__(self, name, email, address, account_type):
        self.name = name
        self.email = email
        self.address = address
        self.account_type = account_type
        self.balance = 0
        self.loan_limit = 2
        self.loans_taken = 0
        self.transaction_history = []
        self.account_number = random.randint(0, 100)



    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transaction_history.append(f'Deposit: +${amount}')
            print(f'Deposited ${amount}. New balance: ${self.balance}')
        else:
            print('invalid deposit amount.')


    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                self.transaction_history.append(f'Withdrawal: -${amount}')
                print(f'Withdrawn ${amount}. New balance: ${self.balance}')
            else:
                print('Withdrawal amount exceeded.')
        else:
            print('Invalid withdrawal amount.')


    def check_balance(self):
        return self.balance


    def check_transaction_history(self):
        for num in self.transaction_history:
            print(num)


    def take_a_loan(self, loan_amount):
        if self.loans_taken < self.loan_limit:
            if loan_amount > 0:
                self.balance += loan_amount
                self.loans_taken += 1
                self.transaction_history.append(f'Loan Taken: +${loan_amount}')
                print(f'Loan of ${loan_amount} taken. New balance: ${self.balance}')
            else:
                print('invalid loan amount.')

        else:
            print('You have reached the maximum loan limit.')
        

class Admin:
    def __init__(self):
        self.users = []

    def create_account(self, name, email, address, account_type):
        user = User(name, email, address, account_type)
        self.users.append(user)
        return user

    def delete_account(self, user):
        self.users.remove(user)

    def see_user_accounts(self):
        for user in self.users:
            print(f'Account Number: {user.account_number}, Name: {user.name}, Balance: ${user.balance}')


    def check_total_balance(self):
        total_balance = sum(user.balance for user in self.users)
        print(f'Total Balance of the Bank : ${total_balance}')


    def check_total_loan_amount(self):
        total_loans = sum(user.balance for user in self.users if user.loans_taken > 0)
        print(f'Total Loan Amount : ${total_loans}')


    def loan_feature(self, enable=True):
        for user in self.users:
            if enable:
                user.loan_limit = 2
            else:
                user.loan_limit = 0


def create_user(admin):
    name = input('Enter Your Name: ')
    email = input('Enter Your Email: ')
    address = input('Enter Your Address: ')
    account_type = input('Enter account type -> Savings or Current: ')
    return admin.create_account(name, email, address, account_type)


def main():
    admin = Admin()

    while True:
        print('\nBank Management System')
        print('\n1. USER ⇒')
        print('2. ADMIN ⇒')
        print('3. Exit')
        op = int(input('ENTER YOUR OPTION: '))


        if op == 1:
            print('\n------ User List ------')
            print('1. Create User Account')
            print('2. Deposit')
            print('3. Withdraw')
            print('4. Balance')
            print('5. Transaction History')
            print('6. Take Loan Bank')

            user_op = int(input('ENTER YOUR OPTION: '))


            if user_op == 1:
                user = create_user(admin)
                print(f'Account created successfully. Account Number: {user.account_number}')
            elif user_op == 2:
                account_number = int(input('Enter your account number: '))
                user = next((num for num in admin.users if num.account_number == account_number), None)
                if user:
                    amount = int(input('Enter the deposit amount: $'))
                    user.deposit(amount)
                else:
                    print('Account does not exist.')

            elif user_op == 3:
                account_number = int(input('Enter your account number: '))
                user = next((num for num in admin.users if num.account_number == account_number), None)
                if user:
                    amount = float(input('Enter the withdrawal amount: $'))
                    user.withdraw(amount)
                else:
                    print('Account does not exist.')


            elif user_op == 4:
                account_number = int(input('Enter your account number: '))
                user = next((num for num in admin.users if num.account_number == account_number), None)
                if user:
                    balance = user.check_balance()
                    print(f'Current Balance: ${balance}')
                else:
                    print('Account does not exist.')


            elif user_op == 5:
                account_number = int(input('Enter your account number: '))
                user = next((num for num in admin.users if num.account_number == account_number), None)
                if user:
                    print('Transaction History:')
                    user.check_transaction_history()
                else:
                    print('Account does not exist.')


            elif user_op == 6:
                account_number = int(input('Enter your account number: '))
                user = next((num for num in admin.users if num.account_number == account_number), None)
                if user:
                    loan_amount = float(input('Enter the loan amount: $'))
                    user.take_a_loan(loan_amount)
                else:
                    print('Account does not exist.')


        elif op == 2:
            print('\n------ Admin List ------')
            print('1. Create User Account')
            print('2. Delete User Account')
            print('3. User Accounts List')
            print('4. Total Bank Balance')
            print('5. Total Loan Amount')
            print('6. Can on or off the loan feature of the bank')


            admin_op =int(input('ENTER YOUR OPTION: '))

            if admin_op == 1:
                user = create_user(admin)
                print(f'Account created successfully. Account Number: {user.account_number}')


            elif admin_op == 2:
                admin.see_user_accounts()
                account_number = int(input('Enter the account number to delete: '))
                user_to_delete = next((num for num in admin.users if num.account_number == account_number), None)
                if user_to_delete:
                    admin.delete_account(user_to_delete)
                    print(f'User {user_to_delete.name} has been deleted.')
                else:
                    print('Account does not exist.')

            elif admin_op == 3:
                admin.see_user_accounts()

            elif admin_op == 4:
                admin.check_total_balance()

            elif admin_op == 5:
                admin.check_total_loan_amount()

            elif admin_op == 6:
                index = input('Can on or off the loan feature of the bank -> on : off: ').lower()
                if index == 'on':
                    admin.loan_feature(enable=True)
                elif index == 'off':
                    admin.loan_feature(enable=False)

        elif op == 3:
            print('Thank You Sir!')
            break
        else:
            print('invalid option. Please try again!')


if __name__ == '__main__':
    main()
